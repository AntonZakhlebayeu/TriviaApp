import pickle

from aioredis import from_url
from settings import settings

from trivia_microservice.models.statistics import StatisticsModel

redis = from_url(settings.REDIS_URI)


async def get_statistics(id: int):
    read_dict = await redis.get(id)
    if read_dict is None:
        read_dict = await set_default_statistics(id)
    return pickle.loads(read_dict)


async def set_default_statistics(id: int):
    await redis.set(
        id,
        pickle.dumps(
            StatisticsModel(
                amount_of_answers=0, amount_of_correct_answers=0
            ).dict()
        ),
    )

    return await redis.get(id)


async def set_statistics(id: int, answer: bool):
    read_dict = await redis.get(id)
    statistics = pickle.loads(read_dict)
    if answer:
        statistics["amount_of_correct_answers"] = (
            statistics.get("amount_of_correct_answers") + 1
        )
    statistics["amount_of_answers"] = statistics.get("amount_of_answers") + 1
    await redis.set(id, pickle.dumps(statistics))
