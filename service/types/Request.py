import enum
from typing import Union

from pydantic import BaseModel


class RequestType(enum.Enum):
    # request starts with 1, code length - 3
    # answers starts with 2, code length - 3
    AUTHENTICATION_REQUEST = 101
    REGISTRATION_REQUEST = 102
    CODE_VERIFICATION_REQUEST = 103
    EMAIL_VERIFICATION_REQUEST = 104


class RegistrationRequest(BaseModel):
    login: str
    email: str
    first_name: str
    last_name: str
    password: str


class AuthenticationRequest(BaseModel):
    login: str
    password: str


class EmailValidationRequest(BaseModel):
    login: str
    email: str


class CodeValidationRequest(BaseModel):
    email: str
    email_code: int


class Request(BaseModel):
    type: RequestType
    data: Union[RegistrationRequest,
                AuthenticationRequest,
                CodeValidationRequest,
                EmailValidationRequest]
