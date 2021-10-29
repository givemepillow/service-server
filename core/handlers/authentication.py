from loguru import logger

from core.converters import AnswerConstructor
from core.security import Cryptographer, PasswordManager
from database import Database
from core.types import ResponseType


async def authentication(request):
    if request.data.email and not await Database.exists_email(email=request.data.email):
        logger.info(
            f"Отклонена аутентификация (Неверный адрес электронной почты.) "
            f"{request.data.email}: "
            f"{request.ip}")
    elif request.data.login and not await Database.exists_login(login=request.data.login):
        logger.info(
            f"Отклонена аутентификация (Неверный логин.) "
            f"{request.data.login}: "
            f"{request.ip}")
    elif not request.data.login and not request.data.email:
        logger.warning(
            f"Отклонена аутентификация (Пустой логин и пароль.) "
            f"{request.data.login}: "
            f"{request.ip}")
    else:
        try:
            password_from_request = Cryptographer.decrypt(request.data.password)
        except ValueError:
            logger.warning(
                f"Ошибка расшифровки пароля пользователя "
                f"{request.data.login or request.data.email}:"
                f" {request.ip}"
            )
            return AnswerConstructor.create(ResponseType.ERROR, message='Пароль отклонён системой безопасности.')

        password_hash = await Database.get_password(login=request.data.login, email=request.data.email)
        if PasswordManager.verification(password_hash=password_hash, password=password_from_request):
            logger.info(
                f"Подтверждена аутентификация "
                f"{request.data.login or request.data.email}: "
                f"{request.ip}")
            return AnswerConstructor.create(ResponseType.ACCEPT, message='Вход подтверждён.')
        else:
            logger.info(
                f"Отклонена аутентификация (Неверный пароль.) "
                f"{request.data.login or request.data.email}: "
                f"{request.ip}")

    return AnswerConstructor.create(ResponseType.REJECT, message='Неверный логин или пароль.')
