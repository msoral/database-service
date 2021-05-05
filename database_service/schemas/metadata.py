from typing import Dict

from pydantic import AnyHttpUrl, BaseModel


class MetadataBase(BaseModel):
    name: str
    ticker: str
    website: AnyHttpUrl = None
    links: Dict[str, AnyHttpUrl] = None


class MetadataRead(MetadataBase):
    id: int


class MetadataCreate(MetadataBase):
    pass


class MetadataDB(MetadataRead):

    class Config:
        orm_mode = True
