import json
from core.types import Request


class RequestParser:
    @classmethod
    def extract_request(cls, request) -> Request:
        return Request.parse_obj(json.loads(request))
