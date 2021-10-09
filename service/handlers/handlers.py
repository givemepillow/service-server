from .authentication import authentication
from .registration import registration
from .email_verification import email_verification
from .code_verification import code_verification
from service.types import RequestType

handlers = {
    RequestType.AUTHENTICATION_REQUEST: authentication,
    RequestType.REGISTRATION_REQUEST: registration,
    RequestType.EMAIL_VERIFICATION_REQUEST: email_verification,
    RequestType.CODE_VERIFICATION_REQUEST: code_verification
}