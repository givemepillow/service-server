import json
from core.types.Answer import Answer, AnswerType, answers


class AnswerConstructor:

    @classmethod
    def create(cls, answer_type, **kwargs):
        data = dict()
        for field in kwargs:
            data[field] = kwargs[field]
        return Answer(type=answer_type, data=answers[answer_type].parse_obj(data)).json()
