import json
from service.types.Answer import Answer, AnswerType, answers


class AnswerConstructor:

    @classmethod
    def create(cls, answer_type: AnswerType, **kwargs):
        answer = dict()
        answer['type'] = answer_type
        data = dict()
        for field in kwargs:
            if field not in answers[answer_type].__dict__['__fields__'].keys():
                raise ValueError(f"Получено неизвестное поле: {field}.")
            data[field] = kwargs[field]
        answer['data'] = data
        return json.dumps(Answer.parse_obj(answer).json())
