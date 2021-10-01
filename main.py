import asyncio

from database import Connection, Database
from server import Server

user = 'kirill'
password = '41234123'
database = 'messenger'
host = '127.0.0.1'


async def main():
    # Creating connection with database.
    await Connection.connect(user, password, database, host)

    # Init db with connection - creating tables if they not exists.
    await Database.initialization(Connection.connection())

    # Start server
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
