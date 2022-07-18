import asyncio
import pickle

import uvicorn
from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import settings

from trivia_microservice.database import get_statistics, set_statistics

app = FastAPI()
loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
    settings.KAFKA_CHANNEL,
    loop=loop,
    bootstrap_servers=settings.KAFKA_URI,
    group_id=settings.GROUP_ID,
)


origins = [
    settings.ORIGINS,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=[settings.ALLOW_METHODS],
    allow_headers=[settings.ALLOW_HEADERS],
)


@app.on_event("startup")
async def startup_event():
    loop.create_task(consume())


@app.on_event("shutdown")
async def shutdown_event():
    await consumer.stop()


async def consume():
    await consumer.start()
    try:
        async for msg in consumer:
            deserialized_data = pickle.loads(msg.value).get("msg")
            await set_statistics(
                deserialized_data.get("id"), deserialized_data.get("answer")
            )

    finally:
        await consumer.stop()


@app.get("/api/statistics/{id}")
async def user_statistics(id: int):
    return await get_statistics(id)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        debug=True,
        workers=3,
    )
