import asyncpg


class Connection:
    connection: asyncpg.connection

    def __init__(self, user, password, database, host):
        self.user = user
        self.password = password
        self.database = database
        self.host = host

    async def connect(self):
        try:
            self.connection = await asyncpg.connect(
                user=self.user,
                password=self.password,
                database=self.database,
                host=self.host
            )
        except asyncpg.exceptions.InvalidPasswordError as e:
            print(f"{str(e).capitalize()}.")

    def get_connection(self):
        return self.connection

    async def close(self):
        await self.connection.close()
