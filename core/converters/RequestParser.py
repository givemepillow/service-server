import json
from core.types import Request
from core.types.Request import requests


class RequestParser:
    @classmethod
    def extract_request(cls, request) -> Request:
        print(request)
        return Request.parse_obj(json.loads(request))
