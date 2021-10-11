import enum
from typing import Optional

from pydantic import BaseModel


class RequestType(enum.Enum):
    # request starts with 1, code length - 3
    # answers starts with 2, code length - 3
    AUTHENTICATION: int = 101
    REGISTRATION: int = 102
    CODE_VERIFICATION: int = 103
    EMAIL_VERIFICATION: int = 104
    ENCRYPTION_KEY: int = 105


class EncryptionKey(BaseModel):
    pass


class Registration(BaseModel):
    login: str
    email: str
    first_name: str
    last_name: str
    password: str


class Authentication(BaseModel):
    login: str
    password: str


class EmailValidation(BaseModel):
    login: str
    email: str


class CodeValidation(BaseModel):
    email: str
    email_code: int


class Request(BaseModel):
    type: RequestType
    data: Optional[bytes]
    ip: str


requests = {
    RequestType.AUTHENTICATION: Authentication,
    RequestType.ENCRYPTION_KEY: EncryptionKey,
    RequestType.REGISTRATION: Registration,
    RequestType.CODE_VERIFICATION: CodeValidation,
    RequestType.EMAIL_VERIFICATION: EmailValidation
}
