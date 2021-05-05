from .base import Asset


class BinanceAsset(Asset):
    __abstract__ = True
    __table_args__ = {"schema": "binance"}


class Bitcoin(BinanceAsset):
    __tablename__ = "btc"


class Ethereum(BinanceAsset):
    __tablename__ = "eth"


class XRP(BinanceAsset):
    __tablename__ = "xrp"


class Stellar(BinanceAsset):
    __tablename__ = "xlm"


class Chainlink(BinanceAsset):
    __tablename__ = "link"


class BinanceCoin(BinanceAsset):
    __tablename__ = "bnb"


class Polkadot(BinanceAsset):
    __tablename__ = "dot"


class Cardano(BinanceAsset):
    __tablename__ = "ada"


class EOS(BinanceAsset):
    __tablename__ = "eos"


class Monero(BinanceAsset):
    __tablename__ = "xmr"


class Tezos(BinanceAsset):
    __tablename__ = "xtz"


class Cosmos(BinanceAsset):
    __tablename__ = "atom"


class Compound(BinanceAsset):
    __tablename__ = "comp"


class HederaHashgraph(BinanceAsset):
    __tablename__ = "hbar"


class Aave(BinanceAsset):
    __tablename__ = "aave"


class Algorand(BinanceAsset):
    __tablename__ = "algo"


class Synthetix(BinanceAsset):
    __tablename__ = "snx"


class Litecoin(BinanceAsset):
    __tablename__ = "ltc"


ticker_mapper = {
        "btc": Bitcoin,
        "eth": Ethereum,
        "xrp": XRP,
        "xlm": Stellar,
        "link": Chainlink,
        "bnb": BinanceCoin,
        "dot": Polkadot,
        "ada": Cardano,
        "eos": EOS,
        "xmr": Monero,
        "xtz": Tezos,
        "atom": Cosmos,
        "comp": Compound,
        "hbar": HederaHashgraph,
        "aave": Aave,
        "algo": Algorand,
        "snx": Synthetix,
        "ltc": Litecoin,
    }

