from loguru import logger

from core.security import Cryptographer
from database import Database
from core.converters import AnswerConstructor
from core.types import AnswerType
from core.verification import Verify


async def registration(request):
    if await Verify.is_verified(request.data.email, request.data.login):
        try:
            encrypted_password = Cryptographer.decrypt(request.data.password).decode()
        except ValueError:
            logger.warning(
                f"Ошибка расшифровки пароля для пользователя "
                f"{request.data.login or request.data.email}:"
                f" {request.ip}"
            )
            return AnswerConstructor.create(AnswerType.ERROR, message='Ошибка расшифровки пароля.')
        db_answer = await Database.registration(
            login=request.data.login,
            password=encrypted_password,
            first_name=request.data.first_name,
            last_name=request.data.last_name,
            email=request.data.email
        )
        if db_answer:
            logger.info(f"Зарегистрирован новый пользователь {request.data.email}: {request.ip}")
            return AnswerConstructor.create(AnswerType.ACCEPT, info='Регистрация завершена.')
        else:
            logger.info(
                f'Отклонена регистрация нового пользователя (Недопустимые данные.) {request.data.email}: {request.ip}')
            return AnswerConstructor.create(AnswerType.REJECT, cause='Недопустимые данные.')
    else:
        logger.warning(
            f'Отклонена регистрация нового пользователя (Почта или логин не подтверждены.) {request.data.email}: {request.ip}')
        return AnswerConstructor.create(AnswerType.REJECT, cause='Почта или логин не подтверждены.')
