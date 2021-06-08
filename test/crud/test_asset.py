import datetime

from sqlalchemy.orm import Session

from database_service import crud
from database_service.schemas.asset import AssetCreate
from test.utils.utils import random_lower_string, random_ochlv_data


def test_create_asset(dbsession: Session) -> None:
    ticker = random_lower_string()
    timestamp = datetime.datetime.timestamp(datetime.datetime.now())
    data = random_ochlv_data()
    item_in = AssetCreate(ticker=ticker, timestamp=timestamp, **data)
    asset = crud.CRUDAsset().create(db=dbsession, obj_in=item_in)

    assert asset.ticker == ticker
    assert asset.timestamp == timestamp
    assert asset.open == data["open"]
