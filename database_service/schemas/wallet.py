from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel


class Holding(BaseModel):
    ticker: str
    quantity: float
    cost: float


class Portfolio(BaseModel):
    date: datetime = datetime.utcnow()
    assets: List[Holding]


class WalletDB(Holding):
    id: int
    date: datetime

    class Config:
        orm_mode = True
