from src import db


class BaseAsset(db.Model):
    __abstract__ = True

    date = db.Column("date", db.DateTime, primary_key=True)
    open = db.Column("open", db.Float)
    close = db.Column("close", db.Float)
    high = db.Column("high", db.Float)
    low = db.Column("low", db.Float)
    volume = db.Column("volume", db.Float)
    market_cap = db.Column('market_cap', db.Float)


class BinanceAsset(BaseAsset):
    __abstract__ = True
    __table_args__ = {'schema': 'binance'}


class InteractiveBrokerAsset(BaseAsset):
    __abstract__ = True
    __table_args__ = {'schema': 'interactive_brokers'}
