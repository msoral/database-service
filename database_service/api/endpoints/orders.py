from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_service.api import deps
from database_service.common import utils
from database_service.crud import CRUDOrder
from database_service.schemas import order

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=order.OrderRead)
def read_order(
        ticker: str,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
        start_date: datetime = utils.get_last_month(),
        end_date: datetime = datetime.utcnow()
):
    return CRUDOrder(db_model).get_by_date(
        sess, ticker, start_date=start_date, end_date=end_date
    )


@router.get("/{order_id}", response_model=order.OrderRead)
def read_order_by_id(
        order_id: UUID,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
):
    return CRUDOrder(db_model).get(sess, order_id)


@router.post("/", response_model=order.OrderRead)
def create_order(
        order_in: order.OrderCreate,
        sess: Session = Depends(deps.get_session),
        db_model: deps.order = Depends(),
):
    order = CRUDOrder(db_model).create(sess, obj_in=order_in)
    return order
