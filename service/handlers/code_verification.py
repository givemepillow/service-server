from service.converters import AnswerConstructor
from service.handlers.types import Answer
from service.verification import Verify


async def code_verification(request):
    if await Verify.verification(request['email'], request['code']):
        return AnswerConstructor.create(Answer.ACCEPT)
    else:
        return AnswerConstructor.create(Answer.REJECT, message='Неверный код!')