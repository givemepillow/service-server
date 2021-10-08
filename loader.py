from database import Connection, Database
from mail import MailSender
import envfileparser

mail_sender = None


async def initialization():
    global mail_sender
    mail_sender = MailSender.create()

    envs = envfileparser.get_env_from_file()
    # Creating connection with database.
    await Connection.connect(envs['USER'], envs['PASSWORD'], envs['DB'], envs['HOST'])

    # Init db with connection - creating tables if they not exists.
    await Database.initialization(Connection.connection())
