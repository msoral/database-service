from datetime import datetime

from pydantic import BaseModel


# Shared properties
class AssetBase(BaseModel):
    timestamp: float
    open: float
    close: float
    high: float
    low: float
    volume: float


# Properties to return to client
class AssetRead(AssetBase):
    pass


# Properties needed for item creation
class AssetCreate(AssetBase):
    ticker: str


# Properties stored in DB
class AssetDB(AssetBase):

    class Config:
        orm_mode = True
