from src.database import AssetMetadata


def _fetch_by_id(uid, exchange):
    # TODO: Select schema before querying assetmetadata.
    return AssetMetadata.query().filter_by(id=uid)


def get_symbol_by_id(uid, exchange):
    asset = AssetMetadata.query.get(uid)
    return str(asset.ticker)
