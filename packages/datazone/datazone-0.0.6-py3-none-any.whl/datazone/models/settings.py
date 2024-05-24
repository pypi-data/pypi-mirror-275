from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class Profile(BaseModel):
    username: str
    password: str
    server_endpoint: str
    token: Optional[str] = None
    is_default: Optional[bool] = False
    last_login: Optional[datetime] = None

    @property
    def token_url(self):
        return f"{self.server_endpoint}/core/auth/token"

    @property
    def refresh_url(self):
        return f"{self.server_endpoint}/core/auth/refresh"


class Settings(BaseModel):
    profiles: Dict[str, Profile] = {}
