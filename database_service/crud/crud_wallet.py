from sqlalchemy.orm import Session
from typing import Any
import database_service.models.base as model
from database_service.schemas.wallet import WalletDB
from .base import CRUDBase


class CRUDWallet(CRUDBase[model.Wallet, WalletDB, WalletDB]):
    def get_holding(self, db: Session, id: Any, start_date, end_date) -> model.Wallet:
        query = super().get(db, id)
        return query
