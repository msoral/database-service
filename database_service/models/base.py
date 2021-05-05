import uuid

from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from database_service.db.base_class import Base


# TODO: Correctly implement a relationship between metadata and wallet.
class AssetMetadata(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True, nullable=False)
    ticker = Column(String(4), nullable=False)
    website = Column(String)
    links = Column(JSON)

    # @declared_attr
    # def wallet_id(self):
    #     return relationship("Wallet", backref="asset_id")


class Asset(Base):
    __abstract__ = True

    timestamp = Column(Float, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Float)
    market_cap = Column(Float)


class Order(Base):
    __abstract__ = True

    order_id = Column("uuid", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column("date", Float)
    symbol = Column("symbol", String(10))
    status = Column("status", String(16))
    side = Column("side", String(4))
    order_type = Column("order_type", String(20))
    quantity = Column("quantity", Float)
    timeInForce = Column("timeInForce", String(3))
    price = Column("price", Float)
    stopPrice = Column("stopPrice", Float)
    icebergQty = Column("icebergQty", Float)
    optional_parameters = Column("fills", JSON)

    def __repr__(self):
        return f"Status: {self.status}, {self.side}:{self.symbol}#{self.quantity}"


class Wallet(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    ticker = Column(String)
    quantity = Column(Float)
    cost = Column(Float)

    # @declared_attr
    # def asset_id(self):
    #     return Column(Integer, ForeignKey("AssetMetadata.id"), nullable=False)
