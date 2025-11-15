from fastapi import Depends, HTTPException, Header
from asyncpg import Pool
from app.database import get_db_pool


async def validate_client(
    pool: Pool = Depends(get_db_pool),
    x_client_id: str = Header(...),
    x_api_key: str = Header(...),
):
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT client_id FROM api_clients WHERE client_id = $1 AND api_key = $2 AND active = true",
            x_client_id,
            x_api_key,
        )

    if not row:
        raise HTTPException(status_code=401, detail="Invalid API credentials")

    return x_client_id
