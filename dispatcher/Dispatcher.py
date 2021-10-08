from converters import RequestParser
from handlers import handlers


class Handler:
    @classmethod
    async def handle_request(cls, data):
        request = RequestParser.extract_request(data)
        to_send = await handlers[request['type']](request)
        return bytes(to_send, encoding="utf-8")
