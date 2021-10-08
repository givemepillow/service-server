from database import Database
from service.converters import AnswerConstructor
from service.handlers.types import Answer
from service.verification import Verify


async def email_verification(request):
    if not await Database.exists_email(request['email']):
        return AnswerConstructor.create(Answer.REJECT, message='Данный email уже зарегистрирован!')
    if not await Database.exists_login(request['login']):
        return AnswerConstructor.create(Answer.REJECT, message='Данный логин уже зарегистрирован!')
    await Verify.add_code(request['email'])
    return AnswerConstructor.create(Answer.ACCEPT)
