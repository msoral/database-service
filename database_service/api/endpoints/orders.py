from uuid import UUID
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_service import crud, schemas
from database_service.api import deps
from database_service.common import utils


router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=schemas.OrderRead)
def read_order(
        ticker: str,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        start_date: datetime = utils.get_last_month(),
        end_date: datetime = datetime.utcnow()
):
    return crud.CRUDOrder(db_model).get_by_date(
        sess, ticker, start_date=start_date, end_date=end_date
    )


@router.get("/{order_id}", response_model=schemas.OrderRead)
def read_order_by_id(
        order_id: UUID,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
):
    return crud.CRUDOrder(db_model).get(sess, order_id)


@router.post("/", response_model=schemas.OrderRead)
def create_order(
        order_in: schemas.OrderCreate,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
):
    order = crud.CRUDOrder(db_model).create(sess, obj_in=order_in)
    return order
