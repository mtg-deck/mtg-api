import asyncpg
from asyncpg import Pool
from app.config import settings
from fastapi import HTTPException, status

pool: Pool | None = None


async def connect_to_db():
    global pool
    pool = await asyncpg.create_pool(dsn=settings.DATABASE_URL, min_size=2, max_size=10)


async def disconnect_from_db():
    global pool
    if pool:
        await pool.close()
        pool = None


def get_db_pool() -> Pool:
    global pool
    if pool is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection pool is not initialized.",
        )
    return pool
