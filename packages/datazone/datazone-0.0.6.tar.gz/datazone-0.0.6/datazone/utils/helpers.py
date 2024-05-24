import os
import shutil
from pathlib import Path

import typer


def create_path(path_name: str, change_directory: bool = False) -> None:
    path = Path(path_name)
    if path.exists():
        delete = typer.confirm(
            f"There is {path} folder, it will be truncated. Are you sure?",
        )
        if not delete:
            return

        shutil.rmtree(path)

    os.mkdir(path)
    if change_directory:
        os.chdir(path)


def get_datazone_path() -> Path:
    return Path.home() / ".datazone"


def check_host_https(host: str) -> str:
    """
    Check if host starts with https:// or http://, if not, add https:// to the beginning of the host.
    Args:
        host (str): host name
    Returns:
        str: host name with https:// at the beginning
    """
    if not host.startswith("https://") and not host.startswith("http://"):
        return f"https://{host}"
    return host
