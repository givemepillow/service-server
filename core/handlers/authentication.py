from loguru import logger

from core.converters import AnswerConstructor
from core.security import Cryptographer
from database import Database
from core.types import AnswerType


async def authentication(request):
    try:
        password = Cryptographer.decrypt(request.data.password)
    except ValueError:
        logger.warning(
            f"Ошибка расшифровки пароля для пользователя "
            f"{request.data.login or request.data.email}:"
            f" {request.ip}"
        )
        return AnswerConstructor.create(AnswerType.ERROR, message='Ошибка расшифровки пароля.')
    db_answer = await Database.authentication(
        login=request.data.login,
        email=request.data.email,
        password=password
    )
    if db_answer:
        logger.info(
            f"Подтверждена аутентификация "
            f"{request.data.login or request.data.email}: "
            f"{request.ip}")
        return AnswerConstructor.create(AnswerType.ACCEPT, info='Вход подтверждён.')
    else:
        logger.info(
            f"Отклонена аутентификация "
            f"{request.data.login or request.data.email}: "
            f"{request.ip}")
        return AnswerConstructor.create(AnswerType.REJECT, cause='Неверный логин или пароль.')
