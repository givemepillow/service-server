import asyncpg


class DB:
    connection: asyncpg.Connection

    def __init__(self, connection):
        self.connection = connection.get_connection()

    async def create_tables(self):
        with open("sql/authentication_data.sql", "r") as f:
            query = f.read()
            await self.connection.fetch(query)
