from datetime import date, datetime
from typing import List, Union
from sqlalchemy.orm import Session, Query
import database_service.models.base as model
import database_service.schemas.order as schema

from .base import CRUDBase


class CRUDOrder(CRUDBase[model.Order, schema.OrderCreate, schema.OrderById]):
    def get_by_date(
            self,
            db: Union[Session, Query],
            ticker,
            start_date: Union[datetime, date],
            end_date: Union[datetime, date]
    ) -> List[model.Order]:
        pass


