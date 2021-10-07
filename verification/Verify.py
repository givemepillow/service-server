from random import randint, seed
from datetime import datetime
from mail import mail, MailText


class VCode:
    def __init__(self):
        self.time = datetime.now()
        seed(self.time)
        self.code = randint(100000, 999999)
        self.verified = False


class Verify:
    email_codes = dict()

    @classmethod
    def add_code(cls, email):
        code = VCode()
        cls.email_codes[email] = code
        mail.send(email, MailText('Подтверждение почты.', f"Ваш код подтверждения: {code.code}"))

    @classmethod
    def is_verified_email(cls, email):
        return email in cls.email_codes and cls.email_codes[email].verified == True

    @classmethod
    def verification(cls, email, code):
        try:
            if cls.email_codes[email].code == int(code):
                cls.email_codes[email].verified = True
                return True
            else:
                return False
        except KeyError:
            return False

    @classmethod
    def clear_old(cls):
        time = datetime.now()
        for email in cls.email_codes:
            if cls.email_codes[email].time - time > 1000 * 6 * 5:
                del cls.email_codes[email]
