from src.database import AssetMetadata, CoinFactory, StockFactory
from .enums import Exchange




def get_indicators(uid, exchange, start_date=None, end_date=None):
    factory = CoinFactory if exchange == Exchange.BINANCE else StockFactory
    asset_class = factory.create_asset()


def get_metadata(exchange):
    if exchange == Exchange.BINANCE:
        AssetMetadata.query.all()


def get_price():
    pass


def insert_price():
    pass

