from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.auth_routes import router as auth_router
from app.routes.card_routes import router as card_router
from app.database import connect_to_db, disconnect_from_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup: Initializing resources...")
    await connect_to_db()
    print("Connection to database established.")
    yield
    print("Application shutdown: Releasing resources...")
    await disconnect_from_db()
    print("Connection to database closed")


app = FastAPI(title="Cards API", lifespan=lifespan)
app.include_router(auth_router)
app.include_router(card_router)
