from database import Database
from converters import AnswerConstructor
from handlers.types import Answer
from verification import Verify


async def registration(request):
    if await Verify.is_verified_email(request['email']):
        db_answer = await Database.registration(
            request['login'],
            request['password'],
            request['first_name'],
            request['last_name'],
            request['email']
        )
        if db_answer:
            return AnswerConstructor.create(Answer.ACCEPT)
        else:
            return AnswerConstructor.create(Answer.REJECT)
    else:
        return AnswerConstructor.create(Answer.REJECT)
