import uuid
from sqlalchemy.dialects.postgresql import UUID

from src import db


class Order(db.Model):
    __tablename__ = "Order"

    order_id = db.Column("uuid", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol = db.Column("symbol", db.String)
    status = db.Column("status", db.String)
    side = db.Column("side", db.String)
    order_type = db.Column("order_type", db.String)
    quantity = db.Column("quantity", db.Float)
    timeInForce = db.Column("timeInForce", db.String)
    price = db.Column("price", db.Float)
    stopPrice = db.Column("stopPrice", db.Float)
    icebergQty = db.Column("icebergQty", db.Float)
    optionalParams = db.Column("fills", db.JSON)
