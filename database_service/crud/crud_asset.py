from datetime import datetime
from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

import database_service.models.base as model
import database_service.schemas as schema
from database_service.common.enums import Exchanges

from .base import CRUDBase


class CRUDAsset(CRUDBase[model.Asset, schema.Asset, schema.Asset]):
    def get_by_date(
        self, db: Session, asset_id: int, *, start_date: datetime, end_date: datetime
    ) -> List[model.Asset]:
        query = db.query(self.model).order_by(self.model.date).all()

        if (start_date and end_date) is None:
            return query
        elif (start_date and end_date) is not None:
            return query.filter(
                and_(self.model.date >= start_date, self.model.date <= end_date)
            ).all()
        else:
            print("ERROR! Please use start_date and end_date together.")

    def calculate_indicators(self):
        pass
