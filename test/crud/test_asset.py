import datetime

from sqlalchemy.orm import Session

from database_service import crud
from database_service.schemas.asset import AssetCreate
from database_service.api import deps
from test.utils import utils


def test_create_asset(dbsession: Session) -> None:
    ticker = utils.random_ticker()
    timestamp = datetime.datetime.timestamp(datetime.datetime.now())
    data = utils.random_ochlv_data()
    item_in = AssetCreate(ticker=ticker, timestamp=timestamp, **data)
    print(item_in)
    asset = crud.CRUDAsset(deps.asset(ticker)).create(db=dbsession, obj_in=item_in)

    assert asset.ticker == ticker
    assert asset.timestamp == timestamp
    assert asset.open == data["open"]
