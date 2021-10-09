import googleapiclient.errors
from loguru import logger

from .MailService import MailService
from .MailBuilder import MailBuilder


class MailSender:
    service: MailService
    INSTANCE = False

    def __init__(self):
        self.service = MailService()

    @classmethod
    def create(cls):
        if cls.INSTANCE:
            raise Exception('Singleton mail service!')
        cls.INSTANCE = True
        return MailSender()

    @logger.catch
    async def send(self, destination, subject, body):
        try:
            self.service.service.users().messages().send(
                userId="me",
                body=MailBuilder.create(destination, subject, body, '')
            ).execute()
            logger.info(f"Отправлен код по адресу: {destination}")
        except googleapiclient.errors.HttpError:
            logger.error(f"Не удалось отпраить электронное сообщение по адресу {destination}")
