from server.types.Request import Request
from server.types.Answer import Answer
from database import Database
from .RequestParser import RequestParser
from .AnswerConstructor import AnswerConstructor
from verification import Verify


class Handler:
    email_codes = {}

    @classmethod
    async def handle_request(cls, data):
        try:
            request = RequestParser.extract_request(data)
            if RequestParser.assert_request(request, Request.AUTHENTICATION_REQUEST):
                to_send = await cls.__authentication(request)
            elif RequestParser.assert_request(request, Request.REGISTRATION_REQUEST):
                to_send = await cls.__registration(request)
            elif RequestParser.assert_request(request, Request.EMAIL_AND_LOGIN_REQUEST):
                to_send = await cls.__email_and_login(request)
            elif RequestParser.assert_request(request, Request.VERIFICATION_REQUEST):
                to_send = await cls.__verification(request)
            else:
                raise Exception("Серверу не удалось распознать запрос :(")
        except Exception as e:
            to_send = AnswerConstructor.create(Answer.ERROR, str(e))
        return bytes(to_send, encoding="utf-8")

    @classmethod
    async def __registration(cls, request):
        if await Verify.is_verified_email(request['email']):
            db_answer = await Database.registration(
                request['login'],
                request['password'],
                request['first_name'],
                request['last_name'],
                request['email']
            )
            if db_answer:
                return AnswerConstructor.create(Answer.ACCEPT)
            else:
                return AnswerConstructor.create(Answer.REJECT)
        else:
            return AnswerConstructor.create(Answer.REJECT)

    @classmethod
    async def __authentication(cls, request):
        db_answer = await Database.authentication(
            request['login'],
            request['password']
        )
        if db_answer:
            return AnswerConstructor.create(Answer.ACCEPT)
        else:
            return AnswerConstructor.create(Answer.REJECT)

    @classmethod
    async def __email_and_login(cls, request):
        if not await Database.exists_email(request['email']):
            return AnswerConstructor.create(Answer.REJECT, 'Данный email уже зарегистрирован!')
        if not await Database.exists_login(request['login']):
            return AnswerConstructor.create(Answer.REJECT, 'Данный логин уже зарегистрирован!')
        await Verify.add_code(request['email'])
        return AnswerConstructor.create(Answer.ACCEPT)

    @classmethod
    async def __verification(cls, request):
        if await Verify.verification(request['email'], request['code']):
            return AnswerConstructor.create(Answer.ACCEPT)
        else:
            return AnswerConstructor.create(Answer.REJECT, 'Неверный код!')
