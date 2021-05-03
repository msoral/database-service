from fastapi import APIRouter

from database_service.common.enums import Exchanges

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/")
def read_order(exchange: Exchanges):
    pass


@router.get("/{order_id}")
def read_order_by_id(exchange: Exchanges, order_id: int):
    pass


@router.post("/")
def create_order(exchange: Exchanges):
    pass
