import database_service.models.base as model
from database_service.schemas.asset import AssetDB, AssetRead

from .base import CRUDBase


class CRUDAsset(CRUDBase[model.Asset, AssetDB, AssetRead]):
    pass


