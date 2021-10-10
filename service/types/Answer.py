import enum
from typing import Union

from pydantic import BaseModel


class AnswerType(enum.Enum):
    # request starts with 1, code length - 3
    # answers starts with 2, code length - 3
    ERROR = 201
    REJECT = 202
    ACCEPT = 203


class Error(BaseModel):
    message: str


class Reject(BaseModel):
    cause: str


class Accept(BaseModel):
    pass


class Answer(BaseModel):
    type: AnswerType
    data: Union[
        Error,
        Reject,
        Accept
    ]


answers = {
    AnswerType.ERROR: Error,
    AnswerType.REJECT: Reject,
    AnswerType.ACCEPT: Accept
}
