from loguru import logger

from core.converters import RequestParser, ResponseConstructor
from core.handlers import handlers
from core.types import ResponseType, RequestType


class RequestManager:
    @classmethod
    async def handle_request(cls, data, ip):
        try:
            request = RequestParser.extract_request(data)
            request.ip = ip
        except ValueError as err:
            logger.warning(err)
            return bytes(ResponseConstructor.create(ResponseType.ERROR, message="Невалидный запрос."), encoding="utf-8")

        try:
            to_send = await handlers[RequestType(request.type)](request)
        except KeyError:
            logger.warning('Получен неизвестный тип запроса. Нет соответствующего хендлера.')
            to_send = ResponseConstructor.create(ResponseType.ERROR, message="Запрос не распознан.")

        return bytes(to_send, encoding="utf-8")
