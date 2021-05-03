from uuid import uuid4

from src import db
from src.database import BinanceOrder, IBOrder

from .enums import Exchange
from .helper import fetch_ticker_from_id, filter_with_date


def _select_order_schema(exchange: str):
    if exchange == Exchange.BINANCE:
        return BinanceOrder
    elif exchange == Exchange.IB:
        return IBOrder
    else:
        raise ValueError(f"{exchange} is not a valid exchange.")


def create_order(exchange, **kwargs):
    order = _select_order_schema(exchange)
    order_id = kwargs.pop("id", uuid4())
    new_order = order(order_id=order_id, **kwargs)
    db.session.add(new_order)
    db.session.commit()


def get_order(exchange, asset_id, start_date, end_date):
    order = _select_order_schema(exchange)
    ticker = fetch_ticker_from_id(asset_id)
    query = db.session.query(order).filter(order.symbol.ilike(f"{ticker}%"))
    # This function already returns the values, so no need to return anything.
    return filter_with_date(order, query, start_date, end_date)


def get_order_by_id(exchange, order_id):
    order = _select_order_schema(exchange)
    return db.session.query(order).get(order_id)
