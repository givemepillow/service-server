from core.types.Responses import Response, responses


class ResponseConstructor:

    @classmethod
    def create(cls, answer_type, **kwargs):
        data = dict()
        for field in kwargs:
            data[field] = kwargs[field]
        return Response.construct(
            type=answer_type,
            data=responses[answer_type].parse_obj(data)
        ).json()
