import asyncio


class Server:

    __buffer_size = 1024

    @classmethod
    async def handle(cls, reader, writer):
        data = await reader.read(cls.__buffer_size)
        message = data.decode()
        writer.close()

    @classmethod
    async def start(cls):
        await cls.main()

    @classmethod
    async def main(cls):
        server = await asyncio.start_server(cls.handle, '127.0.0.1', 6767)

        address = server.sockets[0].getsockname()

        async with server:
            await server.serve_forever()
