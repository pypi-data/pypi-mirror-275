import git
from rich import print

from datazone.service_callers.git import GitServiceCaller
from datazone.service_callers.repository import RepositoryServiceCaller


def initialize_git_repo(repository_name: str) -> None:
    server = RepositoryServiceCaller.get_default_server()
    organisation_name = server.get("default_organisation")

    if not organisation_name:
        print("[bold red]Default organisation does not exist![/bold red]")
        return

    session = RepositoryServiceCaller.create_session(
        server_id=server["_id"],
        organisation_name=organisation_name,
        repository_name=repository_name,
    )
    token = session.get("token")

    git_url = f"{GitServiceCaller.get_service_url()}/{token}"

    repo = git.Repo.init()
    print("[green]Repository has initialized[/green]")

    origin = repo.create_remote("origin", git_url)

    origin.fetch()
    repo.git.checkout("master")
    origin.pull()


def is_git_repo():
    try:
        _ = git.Repo()
    except git.exc.InvalidGitRepositoryError:
        return False
    else:
        return True
