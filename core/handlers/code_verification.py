from loguru import logger

from core.converters import AnswerConstructor
from core.types import AnswerType
from core.verification import Verify


async def code_verification(request):
    if await Verify.verification(email=request.data.email, code=request.data.code):
        logger.info(f'Подтверждён код из почты для нового пользователя {request.data.email}: {request.ip}')
        return AnswerConstructor.create(AnswerType.ACCEPT, info='Адрес электронной почты подтверждён.')
    else:
        logger.info(f'Отклонён код подтверждения для нового пользователя '
                    f'{request.data.email} - {request.data.code}: {request.ip}')
        return AnswerConstructor.create(AnswerType.REJECT, cause='Неверный код!')
