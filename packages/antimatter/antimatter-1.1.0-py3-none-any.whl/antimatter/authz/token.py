import os
from typing import Callable

import antimatter_engine as am
from antimatter.authz.base import Authorization
from antimatter.utils import API_TARGET_VERSION, ClientWrapper, get_base_client
from antimatter_api import ApiClient, Configuration, ApiClient


class TokenAuthorization(Authorization):
    def get_client(self) -> ApiClient:
        token = self.auth_client.get_token()
        token_scope = self.auth_client.get_token_scope()
        return self._init_client(token, token_scope)

    def get_session(self) -> am.PySession:
        return self.auth_client.get_session()

    def _init_client(self, token, token_scope):
        client = get_base_client()
        client.configuration.access_token = token
        client._supported_auth_type = token_scope
        return client
