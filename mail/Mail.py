import smtplib


class Mail:
    def __init__(self, user, password):
        try:
            self.__from = user
            self.__server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.__server.ehlo()
            self.__server.login(user, password)
        except smtplib.SMTPAuthenticationError as e:
            print(e)
        except ConnectionRefusedError as e:
            print(e)

    def send(self, to, mail_text):
        mail_text.set_from(self.__from)
        mail_text.set_to(to)
        self.__server.sendmail(self.__from, to, mail_text.get_text())
