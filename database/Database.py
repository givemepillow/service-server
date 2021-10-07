import asyncpg


class Database:
    __connection: asyncpg.Connection
    AUTHENTICATION_QUERY = 'SELECT login FROM users WHERE login = $1'
    REGISTRATION_QUERY = 'INSERT INTO users(login, email, first_name, last_name) VALUES ($1, $2, $3, $4)'

    @classmethod
    async def initialization(cls, connection: asyncpg.Connection):
        cls.__connection = connection
        await cls.create_tables()

    @classmethod
    async def authentication(cls, login, password):
        result = await cls.__connection.fetch(cls.AUTHENTICATION_QUERY, login)
        if len(result) == 0:
            return False
        return True if login == result[0]['login'] else False

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

    @classmethod
    async def create_tables(cls):
        result = await cls.__connection.fetch(
            "select count(*) from information_schema.tables where table_schema='public';")
        if result[0]['count'] == 0:
            await cls.create_table_users()
            await cls.create_table_authentication_data()

    @classmethod
    async def create_table_authentication_data(cls):
        with open("sql/create/authentication_data.sql", "r") as f:
            query = f.read()
            await cls.__connection.execute(query)

    @classmethod
    async def create_table_users(cls):
        with open("sql/create/users.sql", "r") as f:
            query = f.read()
            await cls.__connection.execute(query)
