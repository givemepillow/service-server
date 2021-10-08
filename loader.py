import envfileparser

from mail import MailService

envs = envfileparser.get_env_from_file()

mail = MailService(envs['EMAIL_USER'], envs['EMAIL_PASSWORD'])
