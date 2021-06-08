from typing import Callable, Generator

from fastapi import Depends

from database_service.common.enums import Exchanges, TableType
from database_service.db.session import SessionLocal
from database_service.models import ExchangeFactory


def get_session() -> Generator:
    try:
        sess = SessionLocal()
        yield sess
    finally:
        sess.close()


def get_exchange(exchange: Exchanges):
    return exchange


# This class glues incoming requests to database tables. Below instances of this class are the table types that we have.
# If a different type of table were to be added, a new instance of this class should be instantiated below, with its'
# respective TableType enum.
class ExchangeMapper:
    def __init__(self, table_string: TableType):
        self.table_string = table_string

    def __call__(self, exchange: Exchanges = Depends(get_exchange)) -> Callable:
        return ExchangeFactory.select_class(exchange, self.table_string)


metadata = ExchangeMapper(TableType.metadata)
asset = ExchangeMapper(TableType.asset)
order = ExchangeMapper(TableType.order)
wallet = ExchangeMapper(TableType.wallet)
