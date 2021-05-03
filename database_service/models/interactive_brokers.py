from .base import AssetMetadata, Order, Wallet


class IBMetadata(AssetMetadata):
    __tablename__ = "AssetMetadata"
    __table_args__ = {"schema": "interactive_brokers"}


class IBOrder(Order):
    __tablename__ = "Order"
    __table_args__ = {"schema": "interactive_brokers"}


class IBWallet(Wallet):
    __tablename__ = "Wallet"
    __table_args__ = {"schema": "interactive_brokers"}
