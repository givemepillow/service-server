import json
from service.types import Request


class RequestParser:
    @classmethod
    def extract_request(cls, data) -> Request:
        return Request.parse_raw(json.loads(data))
