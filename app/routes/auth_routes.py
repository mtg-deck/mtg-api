from fastapi import APIRouter, Depends
from app.security.api_key_generator import generate_api_key
from app.database import get_db_pool
from asyncpg import Pool

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/create-client")
async def create_client(pool: Pool = Depends(get_db_pool)):
    client_id = generate_api_key()[:16]
    api_key = generate_api_key()

    async with pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO api_clients (client_id, api_key) VALUES ($1, $2)",
            client_id,
            api_key,
        )

    return {"client_id": client_id, "api_key": api_key}
