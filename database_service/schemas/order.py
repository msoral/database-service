from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel

from database_service.common.enums import OrderSide, OrderStatus, OrderType, TimeInForce


class OrderBase(BaseModel):
    timestamp: float
    symbol: str
    status: OrderStatus
    side: OrderSide
    order_type: OrderType
    quantity: float
    time_in_force = TimeInForce
    price: float
    stop_price: float
    optional_parameters: Optional[Dict[str, object]]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    id: UUID
