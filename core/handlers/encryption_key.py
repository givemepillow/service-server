from loguru import logger

from core.converters import AnswerConstructor
from core.types import AnswerType
from core.security import Cryptographer

__all__ = ['encryption_key']

from database import Database


async def encryption_key(request):
    if request.data.login and not await Database.exists_login(request.data.login):
        answer = AnswerConstructor.create(AnswerType.REJECT, cause='Несуществующий логин.')
        logger.info(f'Попытка получения ключа шифрования по несуществующему логину '
                    f'{request.data.login}: {request.ip}')
    elif request.data.email and not await Database.exists_email(request.data.email):
        answer = AnswerConstructor.create(AnswerType.REJECT, cause='Несуществующий адрес электронной почты.')
        logger.info(f'Попытка получения ключа шифрования по несуществующему адресу электронной почты '
                    f'{request.data.login}: {request.ip}')
    else:
        answer = AnswerConstructor.create(AnswerType.KEY, key=Cryptographer.get_public_key())
        logger.info(f'Выдан публичный ключ для '
                    f'{request.data.email or request.data.login}: {request.ip}')
    return answer
