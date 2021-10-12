from loguru import logger

from database import Database
from core.converters import AnswerConstructor
from core.types import AnswerType
from core.verification import Verify


async def email_verification(request):
    if not await Database.exists_email(request.data.email):
        logger.info(f'Отклонено подтверждение почты для нового пользователя {request.data.email}: {request.ip}')
        return AnswerConstructor.create(AnswerType.REJECT, cause='Данный email уже зарегистрирован!')
    if not await Database.exists_login(request.data.login):
        logger.info(f'Отклонено подтверждение логина для нового пользователя {request.data.login}: {request.ip}')
        return AnswerConstructor.create(AnswerType.REJECT, cause='Данный логин уже зарегистрирован!')
    try:
        await Verify.add_code(email=request.data.email, login=request.data.login)
    except ValueError as err:
        logger.exception(err)
        return AnswerConstructor.create(
            AnswerType.ERROR, message='Не удалось отправить код подтверждения на указанный адрес электронной почты.')
    logger.info(f'Отправлен код подтверждения почты {request.data.email}: {request.ip}')
    return AnswerConstructor.create(AnswerType.ACCEPT, info='Отправлен код на указанный адрес электронной почты.')
