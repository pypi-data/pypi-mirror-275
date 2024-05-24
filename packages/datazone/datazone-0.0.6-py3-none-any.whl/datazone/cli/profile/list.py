from rich.console import Console
from rich.table import Table

from datazone.core.common.settings import SettingsManager

extract_columns = [
    "Name",
    "Host",
    "Username",
    "Default",
]


def list_func():
    settings = SettingsManager.get_settings()

    console = Console()

    table = Table(*extract_columns)
    for name, profile in settings.profiles.items():
        values = [
            name,
            profile.server_endpoint,
            profile.username,
            "Yes" if profile.is_default else "No",
        ]
        table.add_row(*values)
    console.print(table)
