from loguru import logger

from core.security import Cryptographer
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
        connection = await Connection.create(envs['DB_USER'], envs['DB_PASSWORD'], envs['DB_NAME'], envs['DB_HOST'])
        await Database.connect(connection)


class LoggerLoader:
    @classmethod
    def start(cls):
        logger.add('logbook.log',
                   format="{time} {level} {message}",
                   rotation='100 KB',
                   compression='zip'
                   )


class CryptographerLoader:
    @classmethod
    def start(cls):
        Cryptographer.generate_key()
