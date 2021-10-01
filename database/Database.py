import asyncpg


class Database:
    __connection: asyncpg.Connection

    @classmethod
    async def initialization(cls, connection: asyncpg.Connection):
        cls.__connection = connection
        await cls.create_tables()

    @classmethod
    async def create_tables(cls):
        result = await cls.__connection.fetch(
            "select count(*) from information_schema.tables where table_schema='public';")
        if result[0]['count'] == 0:
            await cls.create_table_authentication_data()

    @classmethod
    async def create_table_authentication_data(cls):
        with open("sql/create/authentication_data.sql", "r") as f:
            query = f.read()
            await cls.__connection.fetch(query)
