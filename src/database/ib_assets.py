from .asset import InteractiveBrokerAsset


class Tesla(InteractiveBrokerAsset):
    __tablename__ = "tsla"

# This will be filled as other assets are decided.


class StockFactory:
    ticker_mapper = {
        "tsla": Tesla,

    }

    @classmethod
    def create_asset(cls, asset_ticker, asset_dict):
        return cls.ticker_mapper[asset_ticker](**asset_dict)
