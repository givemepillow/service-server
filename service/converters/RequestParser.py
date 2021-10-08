import json


class RequestParser:
    @classmethod
    def extract_request(cls, data):
        return json.loads(data)
