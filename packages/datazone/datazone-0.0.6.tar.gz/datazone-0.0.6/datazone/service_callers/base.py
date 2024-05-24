from os import environ as env
from abc import ABC

from datazone.core.common.settings import SettingsManager
from datazone.core.connections.session import get_session


class BaseServiceCaller(ABC):
    service_name: str

    @classmethod
    def get_service_url(cls):
        profile = SettingsManager.get_profile()
        service_url = env.get(f"{cls.service_name.upper()}_STATIC_URL")
        if service_url is None:
            service_url = f"{profile.server_endpoint}/{cls.service_name}"

        return service_url

    @classmethod
    def get_session(cls):
        return get_session()


class BaseCrudServiceCaller(BaseServiceCaller):
    service_name: str
    entity_name: str

    def get_service_url(self):
        profile = SettingsManager.get_profile()
        service_url = env.get(f"{self.service_name.upper()}_STATIC_URL")
        if service_url is None:
            service_url = f"{profile.server_endpoint}/{self.service_name}"

        return service_url
