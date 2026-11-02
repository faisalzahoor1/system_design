from pymongo import AsyncMongoClient
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from app.core.config import settings

logging.basicConfig(
    level=logging.INFO,
    format="INFO: %(asctime)s - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):

    client = AsyncMongoClient(settings.MONGODB_URL)
    try:
        await client.admin.command("ping")

        app.state.mongo_client = client
        app.state.db = client[settings.MONGODB_DB_NAME]

        logger.info("MongoDb Connected Successfully")

        yield
    finally:
        await client.close()
        logger.exception("MongDb Disconnected")
