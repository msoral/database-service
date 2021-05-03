from importlib import import_module

from .base import AssetMetadata, Order, Wallet


class BinanceMetadata(AssetMetadata):
    __tablename__ = "AssetMetadata"
    __table_args__ = {"schema": "binance"}


class BinanceOrder(Order):
    __tablename__ = "Order"
    __table_args__ = {"schema": "binance"}


class BinanceWallet(Wallet):
    __tablename__ = "Wallet"
    __table_args__ = {"schema": "binance"}
