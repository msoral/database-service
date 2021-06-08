from loguru import logger

from database_service.common.enums import Exchanges, TableType

from .base import *
from .binance_assets import ticker_mapper as binance
from .ib_assets import ticker_mapper as ib


class AssetFactory:
    """
    This class is used to create individual asset tables that hold the ochlv data. List of assets are in seperate python
    folders. e.g. `binance_assets.py`
    """
    def __init__(self, ticker_mapper):
        self.ticker_mapper = ticker_mapper

    def create_asset_class(self, ticker) -> Asset:
        assert ticker in self.ticker_mapper
        return self.ticker_mapper[ticker]


class ExchangeFactory:
    """
    This class creates a factory to generate the corresponding class for a given exchange. Notice that select_class
    function returns a class or a function depending on the table type. This is because another factory is needed to
    create individual assets and this select_class function does not have access to the ticker data because it is not needed
    for other table types. Another implementation can be considered in the future to make this more explicit.
    """
    class_map = {
        TableType.metadata: AssetMetadata,
        TableType.asset: Asset,
        TableType.order: Order,
        TableType.wallet: Wallet,
    }

    @classmethod
    def select_class(cls, exchange: Exchanges, base_class_string: TableType):
        logger.info("Factory is working...")
        base_class = cls.class_map[base_class_string]
        assert issubclass(base_class, Base)
        subclass = None

        for klass in base_class.__subclasses__():
            subclass = klass if klass.__table_args__["schema"] == exchange else None
            if base_class_string == TableType.asset:
                if exchange == Exchanges.BINANCE:
                    asset_factory = AssetFactory(ticker_mapper=binance)
                else:
                    asset_factory = AssetFactory(ticker_mapper=ib)
                subclass = asset_factory.create_asset_class
                assert callable(subclass)
            logger.debug(f"Subclass: {subclass}")
            if subclass:
                return subclass
        if subclass is None:
            raise KeyError(
                f"Could not find a subclass with schema {exchange} for base class {base_class}"
            )
