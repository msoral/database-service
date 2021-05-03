from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

import database_service.models.base as model
import database_service.schemas.order as schema
from database_service.common.enums import Exchanges

from .base import CRUDBase


class CRUDOrder(CRUDBase[model.Asset, schema.OrderBase, schema.OrderBase]):
    def get_by_asset_id(
        db: Session,
        exchange: Exchanges,
        asset_id: int,
        *,
        start_date: datetime = datetime.now(),
        end_date: datetime = None
    ) -> Optional[model.Asset]:
        query = db.query(model.Asset).filter()

    def create(self):
        pass


order = CRUDOrder(model.Order)
