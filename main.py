import asyncio

import loader
from server import Server


async def main():
    await loader.initialization()
    # Start server
    await Server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
