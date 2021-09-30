import asyncpg


class Database:
    connection: asyncpg.Connection

    def __init__(self, connection):
        self.connection = connection.get_connection()

    async def create_tables(self):
        result = await self.connection.fetch(
            "select count(*) from information_schema.tables where table_schema='public';")
        if result[0]['count'] == 0:
            await self.create_table_authentication_data()

    async def create_table_authentication_data(self):
        with open("sql/create/authentication_data.sql", "r") as f:
            query = f.read()
            await self.connection.fetch(query)

    async def verify_password_hash(self, login, password):
        stmt = await self.connection.prepare("SELECT password_hash FROM authentication_data WHERE login = $1;")
        result = await stmt.fetchval(login)
        return True if result == password else False
