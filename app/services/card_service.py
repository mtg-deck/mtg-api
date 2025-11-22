from asyncpg import Pool
from app.schemas.card_schema import CardList


async def get_card(card_name: str, pool: Pool):
    query = """
        SELECT *
        FROM cards
        WHERE name = $1
    """

    async with pool.acquire() as conn:
        row = await conn.fetchrow(query, card_name)

    return dict(row) if row else None


async def get_many_cards(cards: CardList, pool: Pool):
    query = """
        SELECT *
        FROM cards
        WHERE name = ANY($1)
        ORDER BY array_position($1, name)
    """

    async with pool.acquire() as conn:
        rows = await conn.fetch(query, cards.cards)

    return {"cards": [dict(row) for row in rows]}


async def get_autocomplete(card_name: str, amount: int = 20, pool: Pool | None = None):
    query = """
        SELECT *
        FROM cards
        WHERE name ILIKE '%' || $1 || '%'
        ORDER BY similarity(name, $1) DESC
        LIMIT $2
    """

    if not pool:
        raise RuntimeError("Pool não inicializado, chame connect_to_db() primeiro")

    async with pool.acquire() as conn:
        rows = await conn.fetch(query, card_name, amount)

    return {"cards": [dict(r) for r in rows]}


async def get_autocomplete_prefix(
    card_name: str, amount: int = 20, pool: Pool | None = None
):
    query = """
        SELECT *
        FROM cards
        WHERE name ILIKE $1 || '%'
        ORDER BY name
        LIMIT $2
    """

    if not pool:
        raise RuntimeError("Pool não inicializado, chame connect_to_db() primeiro")
    async with pool.acquire() as conn:
        rows = await conn.fetch(query, card_name, amount)

    return {"cards": [dict(r) for r in rows]}


async def get_autocomplete_auto(card_name: str, pool: Pool, amount: int = 20):
    return await get_autocomplete(card_name, amount, pool=pool)


async def get_top_commanders(pool: Pool):
    query = """
    SELECT cards.*, top_commanders.rank as commander_rank
    FROM cards
    INNER JOIN top_commanders ON cards.name = top_commanders.name
    ORDER BY top_commanders.rank ASC
    """
    if not pool:
        raise RuntimeError("Pool não inicializado, chame connect_to_db() primeiro")
    async with pool.acquire() as conn:
        rows = await conn.fetch(query)
        return {"cards": [dict(r) for r in rows]}
