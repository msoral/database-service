from typing import Dict, List

from pydantic import BaseModel


class Asset(BaseModel):
    timestamp: float
    asset_id: int
    open: float
    close: float
    high: float
    low: float
    volume: float
    market_cap: float

    class Config:
        orm_mode = True


class AssetIndicator(BaseModel):
    timestamp: float
    indicators: Dict[str, float]


class AssetIndicators(BaseModel):
    asset_id: int
    indicator_list: List[AssetIndicator]
