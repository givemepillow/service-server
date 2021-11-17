import asyncio

from loader import DatabaseLoader, MailLoader, LoggerLoader, CryptographerLoader, StatisticLoader
from server import Server


async def main():
    LoggerLoader.start()
    CryptographerLoader.start()
    await DatabaseLoader.start()
    await MailLoader.start()
    await StatisticLoader.start()
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
