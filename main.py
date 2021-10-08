import asyncio

from loader import DatabaseLoader, MailLoader
from server import Server


async def main():
    await DatabaseLoader.start()
    await MailLoader.start()
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
