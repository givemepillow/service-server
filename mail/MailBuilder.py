import base64
from email.mime.text import MIMEText


class MailBuilder:

    __footer = '\n\nДанное сообщение сгенерировано автоматичеки.'

    @classmethod
    def create(cls, destination, subject, body):
        message = MIMEText(body + cls.__footer)
        message['to'] = destination
        message['from'] = 'me'
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
