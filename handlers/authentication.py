from converters import AnswerConstructor
from database import Database
from handlers.types import Answer


async def authentication(request):
    db_answer = await Database.authentication(
        request['login'],
        request['password']
    )
    if db_answer:
        return AnswerConstructor.create(Answer.ACCEPT)
    else:
        return AnswerConstructor.create(Answer.REJECT)
