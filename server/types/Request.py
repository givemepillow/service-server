class Request:
    AUTHENTICATION = 1
    REGISTRATION = 1

    @classmethod
    def assert_request(cls, request, request_type):
        return request['type'] == request_type
