import smtplib


class Mail:
    def __init__(self, user, password):
        try:
            self.__from = user
            self.__server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.__server.ehlo()
            self.__server.login(user, password)
        except smtplib.SMTPAuthenticationError:
            raise Exception("Ошибка аутентификации почтового сервера :(")
        except ConnectionRefusedError:
            raise Exception("Ошибка установик соединения с почтовым сервером :(")

    def send(self, to, mail_text):
        try:
            mail_text.set_from(self.__from)
            mail_text.set_to(to)
            self.__server.sendmail(self.__from, to, mail_text.get_text())
        except smtplib.SMTPRecipientsRefused:
            raise Exception("Не удалось отправить код по указанному адресу :(")


mail_instance = Mail('kirilllapushinskiy.bot@gmail.com', '2002K3r1llk4#BOT')
