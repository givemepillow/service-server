class MailText:
    __from = None
    __to = None
    __subject = 'Без темы.'
    __body = 'Пустое сообщение.'

    def __init__(self, subject=__subject, body=__body):
        self.__subject = subject
        self.__body = body

    def get_text(self):
        if self.__from is None and self.__to is None:
            raise Exception("Необходимо указать отправителя и получателя!")
        return f"""From: {self.__from}\n""" \
               f"""To: {self.__to}\n""" \
               f"""Subject: {self.__subject}\n""" \
               f"""\n{self.__body}\n""".encode('utf-8')

    def set_from(self, mail_from):
        self.__from = mail_from

    def set_to(self, mail_to):
        self.__to = mail_to
