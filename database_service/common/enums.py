from enum import Enum


class TableType(Enum):
    metadata = "metadata"
    asset = "asset"
    order = "order"
    wallet = "wallet"


class Exchanges(str, Enum):
    BINANCE = "binance"
    IB = "interactive_brokers"


class OrderSide(str, Enum):
    buy = "BUY"
    sell = "SELL"


class OrderType(str, Enum):
    market = "MARKET"
    limit = "LIMIT"
    stop_loss = "STOP_lOSS"
    stop_loss_limit = "STOP_LOSS_LIMIT"
    take_profit = "TAKE_PROFIT"
    take_profit_limit = "TAKE_PROFIT_LIMIT"
    limit_maker = "LIMIT_MAKER"


class OrderStatus(str, Enum):
    new = "NEW"
    partially_filled = "PARTIALLY_FILLED"
    filled = "FILLED"
    cancelled = "CANCELLED"
    pending_cancel = "PENDING_CANCEL"
    rejected = "REJECTED"
    expired = "EXPIRED"


class TimeInForce(str, Enum):
    gtc = "GTC"  # GOOD TILL CANCELLED
    ioc = "IOC"  # IMMEDIATE OR CANCEL
    fok = "FOK"  # FILL OR KILL
