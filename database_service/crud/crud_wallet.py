from datetime import date
from typing import Any, List, Union

from sqlalchemy.orm import Session

import database_service.models.base as model
from database_service.schemas.wallet import WalletCreate, WalletUpdate

from .base import CRUDBase


class CRUDWallet(CRUDBase[model.Wallet, WalletCreate, WalletUpdate]):
    def get_holding(self, db: Session, ticker: Any, start_date: date, end_date: date) -> \
            Union[List[model.Wallet], model.Wallet]:
        base_query = db.query(self.model).filter(self.model.ticker == ticker)
        query = super().get_by_date(base_query, start_date=start_date, end_date=end_date)

        return query

    def get_portfolio(self, db: Session) -> model.Wallet:
        return db.query(self.model).filter(model.Wallet.date == date.today()).all()

    def get_portfolio_history(self, db: Session, *, start_date: date, end_date: date) -> List[model.Wallet]:
        pass
