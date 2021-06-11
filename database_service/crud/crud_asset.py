from sqlalchemy.orm import Session
from loguru import logger
import database_service.models.base as model
from database_service.schemas.asset import AssetCreate, AssetDB, AssetRead

from .base import CRUDBase


class CRUDAsset(CRUDBase[model.Asset, AssetCreate, AssetRead]):
    def create(self, db: Session, *, obj_in: AssetCreate) -> model.Asset:
        obj_in = obj_in.dict()
        obj_in.pop("ticker")
        logger.debug(obj_in)
        obj_in = AssetDB(**obj_in)
        logger.debug(obj_in)
        return super().create(db, obj_in=obj_in)
