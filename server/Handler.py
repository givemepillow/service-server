from server.types.Request import Request
from server.types.Answer import Answer
from database import Database
from .RequestParser import RequestParser
from .AnswerConstructor import AnswerConstructor


class Handler:
    @classmethod
    async def handle_request(cls, data):
        try:
            request = RequestParser.extract_request(data)
            if RequestParser.assert_request(request, Request.AUTHENTICATION_REQUEST):
                to_send = await cls.__authentication(request)
            elif RequestParser.assert_request(request, Request.REGISTRATION_REQUEST):
                to_send = await cls.__registration(request)
            else:
                to_send = AnswerConstructor.create(Answer.ERROR, "Undefined request.")
        except Exception:
            to_send = AnswerConstructor.create(Answer.ERROR, "Unexpected error.")
        return bytes(to_send, encoding="utf-8")

    @classmethod
    async def __registration(cls, request):
        db_answer = await Database.registration(
            request['login'],
            request['password'],
            request['first_name'],
            request['last_name'],
            request['email']
        )
        if db_answer:
            return AnswerConstructor.create(Answer.REGISTRATION_ACCEPTED)
        else:
            return AnswerConstructor.create(Answer.REGISTRATION_REJECTED)

    @classmethod
    async def __authentication(cls, request):
        db_answer = await Database.authentication(
            request['login'],
            request['password']
        )
        if db_answer:
            return AnswerConstructor.create(Answer.AUTHENTICATION_ACCEPTED)
        else:
            return AnswerConstructor.create(Answer.AUTHENTICATION_REJECTED)
