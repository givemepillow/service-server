from database import Database
from service.converters import AnswerConstructor
from service.handlers.types import Answer
from service.verification import Verify


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
