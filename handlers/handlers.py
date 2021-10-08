from .authentication import authentication
from .registration import registration
from .email_verification import email_verification
from .code_verification import code_verification
from handlers.types import Request

handlers = {
    Request.AUTHENTICATION_REQUEST: authentication,
    Request.REGISTRATION_REQUEST: registration,
    Request.EMAIL_VERIFICATION_REQUEST: email_verification,
    Request.CODE_VERIFICATION_REQUEST: code_verification
}
