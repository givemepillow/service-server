import json


class AnswerConstructor:
    @classmethod
    def create(cls, answer_type, message=''):
        return json.dumps({
            'type': answer_type,
            'message': message
        })
