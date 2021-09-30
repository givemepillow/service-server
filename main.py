import asyncio

from database import Connection, DB

user = 'kirill'
password = '41234123'
database = 'messenger'
host = '127.0.0.1'


async def main():
    connection = Connection(user, password, database, host)
    await connection.connect()

    db = DB(connection)
    await db.create()
    print(await db.get_table_count_info())

    await db.connection.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
