from core.converters import ResponseConstructor
from core.types import ResponseType
from statistics import Statistics


async def statistics(_):
    return ResponseConstructor.create(
        ResponseType.STATS,
        clients_count=Statistics.get_clients_count()
    )
