from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.base import engine, Base
from routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

# 라우터 등록
app.include_router(users.router)