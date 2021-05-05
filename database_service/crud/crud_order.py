import database_service.models.base as model
import database_service.schemas.order as schema

from .base import CRUDBase


class CRUDOrder(CRUDBase[model.Order, schema.OrderCreate, schema.OrderById]):
    pass

