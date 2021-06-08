from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel


class WalletBase(BaseModel):
    date: datetime
    ticker: str
    quantity: float
    cost: float


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass


class Portfolio(BaseModel):
    assets: List[WalletBase]


class WalletDB(WalletBase):
    id: int

    class Config:
        orm_mode = True
