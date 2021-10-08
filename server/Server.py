import asyncio

from dispatcher.Dispatcher import RequestManager


class Server:
    __buffer_size = 1024

    @classmethod
    async def handle(cls, reader, writer):
        data = await reader.read(cls.__buffer_size)
        request = data.decode('utf-8')
        answer = await RequestManager.handle_request(request)
        writer.write(answer)
        await writer.drain()
        writer.close()

    @classmethod
    async def start(cls):
        await cls.main()

    @classmethod
    async def main(cls):
        server = await asyncio.start_server(cls.handle, '127.0.0.1', 6767)

        async with server:
            await server.serve_forever()
