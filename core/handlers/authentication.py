from core.converters import AnswerConstructor
from database import Database
from core.data_model import AnswerType


async def authentication(request):
    db_answer = await Database.authentication(
        request.data.login,
        request.data.password
    )
    if db_answer:
        return AnswerConstructor.create(AnswerType.ACCEPT)
    else:
        return AnswerConstructor.create(AnswerType.REJECT)
