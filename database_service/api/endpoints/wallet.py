from datetime import date
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_service.api import deps
from database_service.common import utils
from database_service.crud import CRUDWallet
from database_service.schemas import wallet

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("/", response_model=wallet.WalletUpdate)
def read_holding(
        *,
        ticker: str,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        start_date: date = utils.get_last_month(),
        end_date: date = date.today()
):
    """
    Returns the most recent cost for a given asset

    """
    return CRUDWallet(db_model).get_holding(sess, ticker, start_date, end_date)


@router.get("/all", response_model=List[wallet.WalletUpdate])
def read_portfolio(
        *,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
):
    """
    Returns latest portfolio
    """
    return CRUDWallet(db_model).get_portfolio(sess)


@router.get('/historic', response_model=wallet.WalletUpdate)
def read_portfolio(
        *,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        start_date: date = utils.get_yesterday(),
        end_date: date = date.today()
):
    """
    Returns historic portfolio

    """
    return CRUDWallet(db_model).get_portfolio_history(sess, start_date=start_date, end_date=end_date)


@router.post("/", response_model=wallet.WalletCreate)
def create_holding(
        *,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        wallet_in: wallet.WalletCreate
):
    return CRUDWallet(db_model).create(sess, obj_in=wallet_in)
