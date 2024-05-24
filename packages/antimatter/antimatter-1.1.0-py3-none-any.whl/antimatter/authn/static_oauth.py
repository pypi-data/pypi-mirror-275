from antimatter.authn.base import OAuthAuthentication
from antimatter.auth.config.tokens import StaticToken, OidcToken

class StaticOAuthAuthentication(OAuthAuthentication):
    """
    A static authentication agent uses a static oauth token.
    This implementation does not know about the token's expiration or it's validity.
    It's up to the upstream service to handle the token's expiration and validity.
    """

    def __init__(self, token: str):
        self.token = token

    def authenticate(self):
        pass

    def get_token(self):
        return self.token

    def needs_refresh(self):
        return False

    def get_token_scope(self):
        return 'google_oauth_token'
    
    def get_session(self):
        raise Exception("Session cannot be created for static oauth token")

    def get_domain_id(self):
        raise Exception("Domain id cannot be retrieved for static oauth token")

    def get_email(self):
        raise Exception("Email cannot be retrieved for static oauth token")

    def get_config_token(self) -> OidcToken:
        return StaticToken(
            token=self.token
        )
