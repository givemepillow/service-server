import json
from json import JSONDecodeError

from core.types import Request


class RequestParser:
    @classmethod
    def extract_request(cls, request) -> Request:
        try:
            request = Request.parse_obj(json.loads(request))
        except JSONDecodeError:
            raise ValueError('Получен невалидный запрос.')
        return request
