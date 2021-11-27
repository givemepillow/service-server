from database import Database


class Statistics:
    __online_users = dict()
    __online_ports = dict()
    __all = 0

    @classmethod
    async def connection(cls, port, user_id=None):
        print(port, user_id)
        if user_id:
            print(f"connection {user_id=}")
            if user_id not in cls.__online_users:
                cls.__online_users[user_id] = set()
            cls.__online_users[user_id].add(port)
        cls.__online_ports[port] = user_id

    @classmethod
    async def disconnection(cls, port):
        if port in cls.__online_ports:
            user_id = cls.__online_ports[port]
            del cls.__online_ports[port]
            print(f"disconnection {user_id=}")
            if user_id:
                cls.__online_users[user_id].discard(port)
                if len(cls.__online_users[user_id]) == 0:
                    del cls.__online_users[user_id]

    @classmethod
    async def update_all(cls):
        cls.__all = await Database.get_count()

    @classmethod
    def get_offline_count(cls):
        _count = cls.__all - len(cls.__online_users)
        return _count if _count > 0 else 0

    @classmethod
    def get_online_count(cls):
        return len(cls.__online_users)
