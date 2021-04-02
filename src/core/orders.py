from src.database import Order
from .helper import get_symbol_by_id


def add_order():
    pass


def get_order(exchange, asset_id=None, start_date=None, end_date=None):
    if asset_id is not None:
        symbol = get_symbol_by_id(asset_id, exchange)
    if (start_date and end_date) is None:
        Order.query().filter_by(symbol=symbol)


def get_order_by_id():
    pass


