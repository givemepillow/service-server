import json


class AnswerConstructor:
    DEFAULT_MESSAGE = 'Unexpected error.'

    @classmethod
    def create(cls, answer_type, **kwargs):
        return json.dumps({
            'type': answer_type,
            'message': kwargs['message'] if 'message' in kwargs else cls.DEFAULT_MESSAGE
        })
