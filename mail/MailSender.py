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

    async def __call__(self, destination, subject, body):
        return self.service.service.users().messages().send(
            userId="me",
            body=MailBuilder.create(destination, subject, body)
        ).execute()
