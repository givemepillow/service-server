import asyncpg


class Connection:
    __connection: asyncpg.connection

    @classmethod
    async def connect(cls, user, password, database, host):
        try:
            cls.__connection = await asyncpg.connect(
                user=user,
                password=password,
                database=database,
                host=host
            )
        except asyncpg.exceptions.InvalidPasswordError as e:
            print(f"{str(e).capitalize()}.")

    @classmethod
    def connection(cls):
        return cls.__connection

    @classmethod
    async def close(cls):
        await cls.__connection.close()
