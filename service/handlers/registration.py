from database import Database
from service.converters import AnswerConstructor
from service.types import AnswerType
from service.verification import Verify


async def registration(request):
    if await Verify.is_verified_email(request.data.email):
        db_answer = await Database.registration(
            request.data.login,
            request.data.password,
            request.data.first_name,
            request.data.last_name,
            request.data.email
        )
        if db_answer:
            return AnswerConstructor.create(AnswerType.ACCEPT)
        else:
            return AnswerConstructor.create(AnswerType.REJECT)
    else:
        return AnswerConstructor.create(AnswerType.REJECT)
