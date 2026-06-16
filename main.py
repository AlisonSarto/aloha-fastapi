from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.init import init_db
from routes.api import router as app_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan
)


app.include_router(app_router)
