import json


class AnswerConstructor:
    DEFAULT_MESSAGE = 'Unexpected error.'

    @classmethod
    def create(cls, answer_type, **kwargs):
        json_dict = {
            'type': answer_type,
            'message': kwargs['message'] if 'message' in kwargs else cls.DEFAULT_MESSAGE
        }
        for v in kwargs:
            json_dict[v] = kwargs[v]
        return json.dumps(json_dict)
