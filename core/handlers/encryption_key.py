from loguru import logger

from core.converters import AnswerConstructor
from core.types import AnswerType
from core.security import Cryptographer

__all__ = ['encryption_key']


async def encryption_key(request):
    answer = AnswerConstructor.create(AnswerType.KEY, key=Cryptographer.get_public_key())
    logger.info(f'Выдан публичный ключ для {request.data.email}: {request.ip}')
    return answer
