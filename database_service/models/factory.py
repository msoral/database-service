from database_service.common.enums import TableType

from .base import *


# This function actually generates schema specific tables but the it is called `ExchangeFactory` to avoid confusion with
# OpenAPI schemas.
class ExchangeFactory:
    class_map = {
        TableType.metadata: AssetMetadata,
        TableType.asset: Asset,
        TableType.order: Order,
        TableType.wallet: Wallet,
    }

    @classmethod
    def select_class(cls, exchange, base_class_string: TableType):
        print("Factory is working...")
        base_class = cls.class_map[base_class_string]
        assert issubclass(base_class, Base)
        subclass = None
        for klass in base_class.__subclasses__():
            subclass = klass if klass.__table_args__["schema"] == exchange else None
            print("------------------Subclass------------------")
            print(subclass)
            if subclass:
                return subclass
        if subclass is None:
            raise NameError(
                f"Could not find a subclass with schema {exchange} for base class {base_class}"
            )
