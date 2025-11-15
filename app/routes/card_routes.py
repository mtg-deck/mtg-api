from fastapi import APIRouter, Depends, HTTPException
from app.security.auth import validate_client
from app.schemas.card_schema import Card, CardList, CardListResponse
from app.services.card_service import (
    get_card,
    get_autocomplete,
    get_many_cards,
)
from app.database import get_db_pool
from asyncpg import Pool

router = APIRouter(prefix="/api/cards", tags=["cards"])


@router.post("/", response_model=CardListResponse)
async def create(
    data: CardList, pool: Pool = Depends(get_db_pool), client=Depends(validate_client)
):
    return await get_many_cards(data, pool=pool)


@router.get("/autocomplete/{card_name}", response_model=CardListResponse)
async def autocomplete(
    card_name: str, pool: Pool = Depends(get_db_pool), client=Depends(validate_client)
):
    cards = await get_autocomplete(card_name, pool=pool)
    if not cards:
        raise HTTPException(404)
    return cards


@router.get("/{card_name}", response_model=Card)
async def retrieve(
    card_name: str, pool: Pool = Depends(get_db_pool), client=Depends(validate_client)
):
    card = await get_card(card_name, pool=pool)
    if not card:
        raise HTTPException(404)
    return card
