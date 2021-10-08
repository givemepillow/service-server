import asyncpg


class Database:
    __connection: asyncpg.Connection
    REGISTRATION_QUERY = 'INSERT INTO users(login, email, first_name, last_name) VALUES ($1, $2, $3, $4)'
    LOGIN_QUERY = 'SELECT login FROM users WHERE login = $1'
    EMAIL_QUERY = 'SELECT email FROM users WHERE email = $1'

    @classmethod
    async def connect(cls, connection: asyncpg.Connection):
        cls.__connection = connection

    @classmethod
    async def authentication(cls, login, password):
        result = await cls.__connection.fetch(cls.LOGIN_QUERY, login)
        if len(result) == 0:
            return False
        return True if login == result[0]['login'] else False

    @classmethod
    async def exists_email(cls, email):
        result = await cls.__connection.fetch(cls.EMAIL_QUERY, email)
        if len(result) == 0:
            return True
        return False

    @classmethod
    async def exists_login(cls, login):
        result = await cls.__connection.fetch(cls.LOGIN_QUERY, login)
        if len(result) == 0:
            return True
        return False

    @classmethod
    async def registration(cls, login, password, first_name, last_name, email):
        try:
            await cls.__connection.fetch(
                cls.REGISTRATION_QUERY,
                login, email, first_name, last_name
            )
            return True
        except asyncpg.exceptions.CheckViolationError or asyncpg.exceptions.UniqueViolationError as e:
            print(e)
            return False
