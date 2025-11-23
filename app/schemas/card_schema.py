from pydantic import BaseModel
from typing import Optional


class CardList(BaseModel):
    cards: list[str]


class Card(BaseModel):
    id: str
    name: str
    colors: Optional[str] = None
    color_identity: Optional[str] = None
    cmc: Optional[str] = None
    mana_cost: Optional[str] = None
    image: Optional[str] = None
    art: Optional[str] = None
    legal_commanders: Optional[bool] = None
    price: Optional[str] = None
    is_commander: Optional[bool] = None
    edhrec_rank: Optional[int] = None
    type_line: Optional[str] = None


class Commander(Card):
    commander_rank: Optional[int] = None


class CardListResponse(BaseModel):
    cards: list[Card]


class CommanderList(BaseModel):
    cards: list[Commander]
