import asyncpg
from loguru import logger


class Database:
    __connection_pool: asyncpg.pool
    REGISTRATION_QUERY = 'INSERT INTO users(login, email, first_name, last_name, password_hash) ' \
                         'VALUES ($1, $2, $3, $4, $5)'
    LOGIN_QUERY = 'SELECT login FROM users WHERE login = $1'
    EMAIL_QUERY = 'SELECT email FROM users WHERE email = $1'

    @classmethod
    async def connect(cls, connection: asyncpg.Connection):
        cls.__connection_pool = connection

    @classmethod
    async def get_password(cls, email, login):
        async with cls.__connection_pool.acquire() as connection:
            if email:
                result = await connection.fetcho('SELECT password_hash FROM users WHERE email = $1', email)
            else:
                result = await connection.fetch('SELECT password_hash FROM users WHERE login = $1', login)
            return result[0][0]

    @classmethod
    async def exists_email(cls, email):
        async with cls.__connection_pool.acquire() as connection:
            result = await connection.fetch(cls.EMAIL_QUERY, email)
            if len(result) == 0:
                return False
            return True

    @classmethod
    async def exists_login(cls, login):
        async with cls.__connection_pool.acquire() as connection:
            result = await connection.fetch(cls.LOGIN_QUERY, login)
            if len(result) == 0:
                return False
            return True

    @classmethod
    async def registration(cls, login, password, first_name, last_name, email):
        async with cls.__connection_pool.acquire() as connection:
            try:
                await connection.fetch(
                    cls.REGISTRATION_QUERY,
                    login, email, first_name, last_name, password
                )
                return True
            except asyncpg.exceptions.CheckViolationError as e:
                logger.exception(e)
            except asyncpg.exceptions.UndefinedColumnError as e:
                logger.exception(e)
            except asyncpg.exceptions.UniqueViolationError as e:
                logger.exception(e)
            return False
