from service.converters import RequestParser
from service.handlers import handlers


class RequestManager:
    @classmethod
    async def handle_request(cls, data):
        request = RequestParser.extract_request(data)
        to_send = await handlers[request['type']](request)
        return bytes(to_send, encoding="utf-8")
