from src import db
from src.database import BinanceMetadata, CoinFactory, IBMetadata, StockFactory

from .enums import Exchange
from .helper import fetch_ticker_from_id, filter_with_date


def _select_metadata_schema(exchange: str):
    if exchange == Exchange.BINANCE:
        return BinanceMetadata
    elif exchange == Exchange.IB:
        return IBMetadata
    else:
        raise ValueError(f"{exchange} is not a valid exchange.")


def _select_factory_schema(exchange: str):
    if exchange == Exchange.BINANCE:
        return CoinFactory
    elif exchange == Exchange.IB:
        return StockFactory
    else:
        raise ValueError(f"{exchange} is not a valid exchange.")


def get_metadata(exchange):
    metadata = _select_metadata_schema(exchange)
    return db.session.query(metadata).all()


def create_metadata(exchange, **kwargs):
    metadata = _select_metadata_schema(exchange)
    kwargs.pop("id")
    print(kwargs)
    new_metadata = metadata(**kwargs)
    db.session.add(new_metadata)
    db.session.commit()
    return "Success"


def get_price(exchange: str, asset_id, start_date, end_date):
    factory = _select_factory_schema(exchange)
    ticker = fetch_ticker_from_id(asset_id)
    asset = factory.ticker_mapper(ticker)
    query = db.session.query(asset).order_by(asset.date).all()
    return filter_with_date(asset, query, start_date, end_date)


def create_price(exchange: str, **kwargs):
    factory = _select_factory_schema(exchange)
    asset_id = kwargs.pop("asset_id")
    assert asset_id is not None
    ticker = fetch_ticker_from_id(asset_id)
    asset = factory.create_asset(ticker, kwargs)
    db.session.add(asset)
    db.session.commit()
    return "Success"


def get_indicators(exchange, uid, start_date, end_date):
    factory = _select_factory_schema(exchange)
    asset_class = factory.create_asset()
