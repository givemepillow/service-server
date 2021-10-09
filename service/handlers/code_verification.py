from service.converters import AnswerConstructor
from service.types import AnswerType
from service.verification import Verify


async def code_verification(request):
    if await Verify.verification(request.data.email, request.data.code):
        return AnswerConstructor.create(AnswerType.ACCEPT)
    else:
        return AnswerConstructor.create(AnswerType.REJECT, message='Неверный код!')
