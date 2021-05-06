
from src import db
from src.database import BinanceWallet, IBWallet

from .enums import Exchange
from .helper import fetch_ticker_from_id, filter_with_date


def _select_wallet_schema(exchange: str):
    if exchange == Exchange.BINANCE:
        return BinanceWallet
    elif exchange == Exchange.IB:
        return IBWallet
    else:
        raise ValueError(f"{exchange} is not a valid exchange.")


def _create_wallet_entry(exchange, **kwargs):
    wallet = _select_wallet_schema(exchange)
    wallet_entry = wallet(**kwargs)
    db.session.add(wallet_entry)
    db.session.commit()


def get_cost(exchange, asset_id):
    wallet = _select_wallet_schema(exchange)
    base_query = db.session.query(wallet)
    latest_date = base_query.order_by(wallet.date.desc()).first().date
    query = base_query.filter(wallet.date == latest_date).all()
    if asset_id is not None:
        ticker = fetch_ticker_from_id(asset_id)
        query = query.filter(wallet.ticker == ticker)
    cost = 0
    for row in query:
        cost += row.cost
    return cost


def get_holdings(exchange, asset_id, start_date, end_date):
    wallet = _select_wallet_schema(exchange)
    base_query = db.session.query(wallet)
    if start_date is None:
        assert end_date is None
        start_date = base_query.order_by(wallet.date.desc()).first().date
        end_date = start_date
    if asset_id is None:
        query = base_query
    else:
        ticker = fetch_ticker_from_id(asset_id)
        query = base_query.filter(wallet.asset_name == ticker)
    return filter_with_date(wallet, query, start_date, end_date)
