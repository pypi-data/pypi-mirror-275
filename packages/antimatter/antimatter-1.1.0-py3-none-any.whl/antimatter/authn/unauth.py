from antimatter.authn.base import Authentication

class Unauthenticated(Authentication):
    """
    An unauthenticated agent which does not have any authentication.
    Can be used to create a session for an unauthenticated user.
    """

    def authenticate(self):
        pass

    def get_token(self):
        return None

    def needs_refresh(self):
        return False

    def get_token_scope(self):
        return None
    
    def get_session(self):
        raise Exception("Unauthenticated session cannot be created")

    def get_domain_id(self):
        return None

    def get_email(self):
        return None
