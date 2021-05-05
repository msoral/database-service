from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database_service import crud, schemas
from database_service.api import deps
from database_service.common import utils
from datetime import datetime

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("/cost", response_model=schemas.Holding)
def read_cost(
        *,
        ticker: str,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        start_date: datetime = utils.get_last_month(),
        end_date: datetime = datetime.utcnow()
):
    """
    Returns the most recent cost for a given asset

    """
    return crud.CRUDWallet(db_model).get(sess, ticker)


@router.get("/")
def read_portfolio():
    pass
