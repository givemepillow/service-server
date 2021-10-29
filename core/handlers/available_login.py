from loguru import logger

from core.converters import AnswerConstructor
from database import Database
from core.types import ResponseType


async def available_login(request):
    if await Database.exists_login(login=request.data.login):
        return AnswerConstructor.create(ResponseType.REJECT, message="Данный логин уже используется.")
    else:
        return AnswerConstructor.create(ResponseType.ACCEPT, message="Данный логин свободен.")
