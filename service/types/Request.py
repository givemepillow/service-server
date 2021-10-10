import enum
from typing import Union

from pydantic import BaseModel


class RequestType(enum.Enum):
    # request starts with 1, code length - 3
    # answers starts with 2, code length - 3
    AUTHENTICATION = 101
    REGISTRATION = 102
    CODE_VERIFICATION = 103
    EMAIL_VERIFICATION = 104


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
    data: Union[
        Registration,
        Authentication,
        CodeValidation,
        EmailValidation
    ]
