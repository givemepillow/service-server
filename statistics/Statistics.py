from database import Database


class Statistics:
    __online = 0
    __all = 0

    @classmethod
    async def update_all(cls):
        cls.__all = await Database.get_count()

    @classmethod
    def up(cls):
        cls.__online += 1

    @classmethod
    def down(cls):
        cls.__online -= 1

    @classmethod
    def get_offline_count(cls):
        _count = cls.__all - cls.__online
        return _count if _count > 0 else 0

    @classmethod
    def get_online_count(cls):
        return cls.__online
