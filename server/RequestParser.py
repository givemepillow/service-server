import json


class RequestParser:
    @classmethod
    def assert_request(cls, request, request_type):
        return request['type'] == request_type

    @classmethod
    def extract_request(cls, data):
        return json.loads(data)