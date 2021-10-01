import asyncio

import envfileparser

from database import Connection, Database
from server import Server


async def main():
    envs = envfileparser.get_env_from_file()

    # Creating connection with database.
    await Connection.connect(envs['USER'], envs['PASSWORD'], envs['DB'], envs['HOST'])

    # Init db with connection - creating tables if they not exists.
    await Database.initialization(Connection.connection())

    # Start server
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
