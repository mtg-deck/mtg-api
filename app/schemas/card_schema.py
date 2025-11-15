from pydantic import BaseModel
from typing import Optional


class CardList(BaseModel):
    cards: list[str]


class Card(BaseModel):
    name: str
    rarity: Optional[str] = None
    colors: Optional[str] = None
    color_identity: Optional[str] = None
    cmc: Optional[str] = None
    mana_cost: Optional[str] = None
    image: Optional[str] = None
    art: Optional[str] = None
    legal_commanders: Optional[bool] = None
    price: Optional[str] = None
    is_commander: Optional[bool] = None


class CardListResponse(BaseModel):
    cards: list[Card]
