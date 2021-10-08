import smtplib

from .MailText import MailText


class MailService:
    def __init__(self, user, password):
        try:
            self.__from = user
            self.__server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.__server.ehlo()
            self.__server.login(user, password)
        except smtplib.SMTPAuthenticationError:
            raise Exception("Ошибка аутентификации почтового сервера :(")
        except ConnectionRefusedError:
            raise ConnectionRefusedError("Ошибка установик соединения с почтовым сервером :(")

    async def send(self, to, mail_text: MailText):
        try:
            mail_text.set_from(self.__from)
            mail_text.set_to(to)
            self.__server.sendmail(self.__from, to, mail_text.get_text())
        except smtplib.SMTPRecipientsRefused:
            raise smtplib.SMTPRecipientsRefused("Не удалось отправить код по указанному адресу :(")

    def create_mail(self, subject, body):
        return MailText(subject, body)
