from datetime import date
from typing import Dict, List

from pydantic import BaseModel


class WalletBase(BaseModel):
    date: date
    ticker: str
    quantity: float
    cost: float


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass

class Portfolio(BaseModel):
    date: date
    assets: List[WalletBase]


class WalletDB(WalletBase):
    id: int
    date: date

    class Config:
        orm_mode = True
