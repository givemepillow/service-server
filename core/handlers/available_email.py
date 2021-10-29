from loguru import logger

from core.converters import AnswerConstructor
from database import Database
from core.types import AnswerType


async def available_email(request):
    if await Database.exists_email(email=request.data.email):
        return AnswerConstructor.create(AnswerType.REJECT, message="Данный email уже зарегистрирован.")
    else:
        return AnswerConstructor.create(AnswerType.ACCEPT, message="Данный email доступен для регистрации.")
