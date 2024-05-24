import uuid
from enum import Enum
from typing import Optional, List, Dict

import git
import typer
from rich import print

from datazone.core.common.config import ConfigReader
from datazone.errors.common import DatazoneServiceError
from datazone.models.config import Config
from datazone.service_callers.crud import CrudServiceCaller
from datazone.service_callers.job import JobServiceCaller
from datazone.utils import git as git_utils


class ChangeType(str, Enum):
    MODIFIED = "modified"
    ADDED = "added"
    DELETED = "deleted"


def git_push_changes(commit_message: Optional[str] = None) -> None:
    """
    Push changes to the repository. If commit message is not provided, it will be generated automatically as uuid.
    Args:
        commit_message (Optional[str]): Optional commit message
    """
    commit_message = commit_message or str(uuid.uuid4())

    repo = git.Repo()
    origin = repo.remotes.origin

    origin.fetch()
    repo.git.checkout("master")

    repo.index.add("*")

    # Remove all deleted files
    deleted_files = [item.a_path for item in repo.index.diff(None) if item.change_type == "D"]
    if deleted_files:
        repo.index.remove(deleted_files, working_tree=True)

    repo.index.commit(commit_message)
    origin.push("master")
    print("[green]Files have pushed to the repository.[/green]:rocket:")


def get_changed_files_and_content() -> List[Dict]:
    """
    Get changed files and content.
    Returns:
        List[Dict]: List of changed files and content
    """
    repo = git.Repo()
    modified_files = [item.a_path for item in repo.index.diff(None) if item.change_type != "D"]
    deleted_files = [item.a_path for item in repo.index.diff(None) if item.change_type == "D"]

    added_files = [item.a_path for item in repo.index.diff("HEAD")]
    untracked_files = repo.untracked_files
    added_files.extend(untracked_files)

    changed_content = []
    for file in modified_files:
        with open(file, "r") as f:
            changed_content.append({"file_name": file, "content": f.read(), "change_type": ChangeType.MODIFIED})

    for file in added_files:
        with open(file, "r") as f:
            changed_content.append({"file_name": file, "content": f.read(), "change_type": ChangeType.ADDED})

    for file in deleted_files:
        changed_content.append({"file_name": file, "change_type": ChangeType.DELETED})

    return changed_content


def check_changes(file: Optional[str] = None) -> bool:
    config_file = ConfigReader(file)
    config_file_content = config_file.get_config_file_content()

    payload = {"config_file_content": config_file_content, "changed_files": get_changed_files_and_content()}
    result = JobServiceCaller.project_check(project_changes=payload)

    for datum in result:
        log_message_templates_by_level = {
            "info": "[bold blue]INFO[/bold blue]",
            "warning": "[bold yellow]WARNING[/bold yellow]",
            "error": "[bold red]ERROR[/bold red]",
        }

        log_level = log_message_templates_by_level.get(datum.get("level"))
        print(f"{log_level} - {datum.get('message')} - {datum.get('entity_value')}")

    if len(result) == 0:
        print("[bold green]There is not any issue.[/bold green]")
    else:
        delete = typer.confirm("Are you sure deploy your code forcefully?")
        return delete
    return True


def deploy(file: Optional[str] = None, commit_message: Optional[str] = None) -> None:
    """
    Deploy project to the repository.
    Args:
        file: path to the custom config file
        commit_message: commit message
    """
    if not git_utils.is_git_repo():
        config_file = ConfigReader(file)

        config: Config = config_file.read_config_file()
        project = CrudServiceCaller(service_name="job", entity_name="project").get_entity_with_id(
            entity_id=str(config.project_id),
        )

        if project.get("repository_name") is None:
            raise DatazoneServiceError

        repository_name: str = project["repository_name"]
        git_utils.initialize_git_repo(repository_name=repository_name)

    print("[bold green]Checking changes...[/bold green]")
    push_changes = check_changes(file)
    if not push_changes:
        return

    print("[bold green]Deploying...[/bold green]")
    git_push_changes(commit_message)
