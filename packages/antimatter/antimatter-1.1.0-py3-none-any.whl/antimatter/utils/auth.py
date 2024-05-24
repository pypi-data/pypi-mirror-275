import antimatter_api as openapi_client
from antimatter import errors
from antimatter_api.exceptions import UnauthorizedException, BadRequestException, NotFoundException
from antimatter_api import ApiClient
from antimatter.utils.constants import ADMIN_VERIFICATION_PROMPT

def authenticate(client: ApiClient, domain_authenticate: openapi_client.DomainAuthenticate, domain_id: str, identity_provider_name: str=None) -> str:
    """
    Authenticate a domain with the given domain_id and domain_authenticate object.
    This function will return the token for the authenticated domain.
    It will try to catch a few specific exceptions and raise a SessionError with a more
    user-friendly message.

    :param client: The client to use for the request.
    :param domain_authenticate: The domain authenticate object to use for the request.
    :param domain_id: The domain ID to authenticate.
    :param identity_provider_name: The identity provider name to authenticate with.
    :return: The token for the authenticated domain.
    """
    try:
        return openapi_client.AuthenticationApi(client).domain_authenticate(
            domain_id=domain_id,
            domain_authenticate=domain_authenticate,
            identity_provider_name=identity_provider_name
        ).token
    except UnauthorizedException as e:
        if e.status == 401:
            raise errors.SessionError(ADMIN_VERIFICATION_PROMPT) from None
        else:
            raise
    except BadRequestException as e:
        if e.status == 400 and hasattr(e.data, 'field') and e.data.field == 'APIKey':
                raise errors.SessionError(f"domain auth error: failed to identify the API key") from None
        else:
            raise
    except NotFoundException as e:
        if e.status == 404 and "antimatter domain" in e.body.lower() and 'does not exist' in e.body.lower():
            raise errors.SessionError(f"domain auth error: '{domain_id}' does not exist") from None
        elif e.status == 404 and "page not found" in e.body.lower():
            raise errors.SessionError(f"domain auth error: failed to identify domain '{domain_id}', please check format") from None
        else:
            raise
    except Exception as e:
        raise errors.SessionError(
            'failed to authenticate domain',
        ) from None
