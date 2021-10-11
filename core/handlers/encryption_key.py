from loguru import logger

from core.converters import AnswerConstructor
from core.data_model import AnswerType
from core.security import Cryptographer


async def encryption_key(request):
    answer = AnswerConstructor.create(AnswerType.KEY, key=Cryptographer.get_public_key())
    logger.info(f"Выдан публичный ключ по адресу: {request.ip}")
    return answer
