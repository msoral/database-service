from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel


class Holding(BaseModel):
    name: str
    quantity: float
    cost: float


class Portfolio(BaseModel):
    date: datetime = datetime.now()
    assets: List[Holding]
