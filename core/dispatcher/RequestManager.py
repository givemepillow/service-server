from json import JSONDecodeError

from loguru import logger

from core.converters import RequestParser, AnswerConstructor
from core.handlers import handlers
from core.types import AnswerType


class RequestManager:
    @classmethod
    async def handle_request(cls, data):
        try:
            request = RequestParser.extract_request(data)
        except ValueError as err:
            logger.warning(err)
            return bytes(AnswerConstructor.create(AnswerType.ERROR, message="Невалидный запрос."), encoding="utf-8")

        try:
            to_send = await handlers[request.type](request)
        except KeyError:
            logger.warning('Получен неизвестный тип запроса.')
            to_send = AnswerConstructor.create(AnswerType.ERROR, message="Запрос не распознан.")

        return bytes(to_send, encoding="utf-8")
