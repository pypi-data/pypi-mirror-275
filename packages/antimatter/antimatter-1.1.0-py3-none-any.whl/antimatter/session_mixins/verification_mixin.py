from typing import Callable, Optional

import antimatter_api as openapi_client
from antimatter import errors
from antimatter.session_mixins.base import BaseMixin
from antimatter.authz import Authorization

class VerificationMixin(BaseMixin):
    """
    Session mixin defining CRUD functionality for verification actions.
    """
    def resend_verification_email(self, email: Optional[str] = None):
        """
        Resend the verification email to the admin contact email. If the session
        was called with an email, that will be used if none is provided.

        :param email: The email to resend the verification email for.
        """
        if not email and not self._email:
            raise errors.SessionVerificationPendingError("unable to resend verification email: email unknown")

        openapi_client.AuthenticationApi(self.authz.get_client()).domain_contact_issue_verify(
            domain_id=self.domain_id,
            domain_contact_issue_verify_request=openapi_client.DomainContactIssueVerifyRequest(
                admin_email=email or self._email,
            )
        )
