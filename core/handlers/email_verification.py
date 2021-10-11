from database import Database
from core.converters import AnswerConstructor
from core.data_model import AnswerType
from core.verification import Verify


async def email_verification(request):
    if not await Database.exists_email(request.data.email):
        return AnswerConstructor.create(AnswerType.REJECT, message='Данный email уже зарегистрирован!')
    if not await Database.exists_login(request.data.login):
        return AnswerConstructor.create(AnswerType.REJECT, message='Данный логин уже зарегистрирован!')
    await Verify.add_code(request.data.email)
    return AnswerConstructor.create(AnswerType.ACCEPT)
