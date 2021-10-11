from core.converters import AnswerConstructor
from core.data_model import AnswerType
from core.verification import Verify


async def code_verification(request):
    if await Verify.verification(request.data.email, request.data.code):
        return AnswerConstructor.create(AnswerType.ACCEPT)
    else:
        return AnswerConstructor.create(AnswerType.REJECT, message='Неверный код!')
