from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_service import crud, schemas
from database_service.api import deps
from database_service.common import utils

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=List[schemas.MetadataRead])
def read_asset_metadata(
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(),
):
    """Returns metadata of all assets"""
    return crud.CRUDMetadata(db_model).get_multi(sess)


@router.get("/{asset_id}", response_model=schemas.MetadataRead)
def read_asset_metadata(
    ticker: str,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(),
):
    """Returns metadata of the asset with given id"""
    return crud.CRUDMetadata(db_model).get(sess, ticker)


@router.post("/", status_code=201, response_model=schemas.MetadataDB)
def create_asset_metadata(
    *,
    metadata_in: schemas.MetadataCreate,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends()
):
    """
    Create new metadata
    """
    metadata = crud.CRUDMetadata(db_model).create(sess, obj_in=metadata_in)
    return metadata


@router.get("/price", response_model=List[schemas.AssetRead])
def read_asset_price(
    ticker: str,
    *,
    sess: Session = Depends(deps.get_session),
    db_model: deps.asset = Depends(),
    start_date: datetime = utils.get_last_month(),
    end_date: datetime = datetime.utcnow()
):
    return crud.CRUDAsset(db_model).get_by_date(
        sess, ticker, start_date=start_date, end_date=end_date
    )


@router.post("/price", response_model=schemas.AssetRead, status_code=201)
def create_asset_price(
        *,
        asset_in: schemas.AssetCreate,
        sess: Session = Depends(deps.get_session),
        db_model: deps.asset = Depends(),
):
    # db_model for assets return AssetFactory.create_asset function, so it needs to be called to return an asset class.
    db_model = db_model(asset_in.ticker)
    print("final model:")
    print(db_model)
    asset = crud.CRUDAsset(db_model).create(sess, obj_in=asset_in)
    return asset
