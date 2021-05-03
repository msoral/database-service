import database_service.models.base as model
import database_service.schemas.metadata as schema

from .base import CRUDBase


class CRUDMetadata(
    CRUDBase[model.AssetMetadata, schema.MetadataCreate, schema.MetadataRead]
):
    pass
