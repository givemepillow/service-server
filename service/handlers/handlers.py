from .authentication import authentication
from .registration import registration
from .email_verification import email_verification
from .code_verification import code_verification
from service.types import RequestType

handlers = {
    RequestType.AUTHENTICATION: authentication,
    RequestType.REGISTRATION: registration,
    RequestType.EMAIL_VERIFICATION: email_verification,
    RequestType.CODE_VERIFICATION: code_verification
}