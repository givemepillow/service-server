import asyncio

from loader import DatabaseLoader, MailLoader, LoggerLoader
from server import Server


async def main():
    LoggerLoader.start()
    await DatabaseLoader.start()
    await MailLoader.start()
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
