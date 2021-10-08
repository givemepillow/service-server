from converters import AnswerConstructor
from handlers.types import Answer
from verification import Verify


async def code_verification(request):
    if await Verify.verification(request['email'], request['code']):
        return AnswerConstructor.create(Answer.ACCEPT)
    else:
        return AnswerConstructor.create(Answer.REJECT, message='Неверный код!')