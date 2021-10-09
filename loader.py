from loguru import logger

from database import Connection, Database
from mail import MailSender
import envfileparser


class MailLoader:
    sender: MailSender

    @classmethod
    async def start(cls):
        cls.sender = MailSender.create()


class DatabaseLoader:
    @classmethod
    async def start(cls):
        envs = envfileparser.get_env_from_file()
        # Creating connection with database.
        connection = await Connection.create(envs['USER'], envs['PASSWORD'], envs['DB'], envs['HOST'])
        await Database.connect(connection)


class LoggerLoader:
    @classmethod
    def start(cls):
        logger.add('logbook.log',
                   format="{time} {level} {message}",
                   rotation='100 KB',
                   compression='zip'
                   )
