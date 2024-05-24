import os

import antimatter_engine as am
import antimatter_api as openapi_client
from antimatter.authn.base import Authentication
from antimatter.utils import decode_token, is_token_valid, authenticate, get_base_client
from antimatter.auth.config.profiles import Profile
from antimatter.auth.config.auth_config import AuthConfig


class ApiKeyAuthentication(Authentication):
    """
    This is an agent which uses an API key for authentication.
    """

    def __init__(self, domain_id: str = None, api_key: str = None):
        self._api_key = api_key
        self._domain_id = domain_id
        self._token = None
        self._session = None

    def needs_refresh(self):
        return not is_token_valid(*decode_token(self._token))

    def authenticate(self):
        self._token = authenticate(
            client=get_base_client(),
            domain_id=self._domain_id,
            domain_authenticate=openapi_client.DomainAuthenticate(token=self._api_key),
        )

    def get_token(self):
        if self.needs_refresh():
            self.authenticate()
        return self._token

    def get_token_scope(self):
        return "domain_identity"

    def get_session(self):
        token = self.get_token()
        # Use the session if it already exists to reuse it's cache
        if self._session is None:
            self._session = am.PySession.new_from_bearer_access_token(self._domain_id, token)
        else:
            self._session.set_bearer_access_token(token)
        return self._session
    
    def get_domain_id(self):
        return self._domain_id

    def get_email(self):
        return None
