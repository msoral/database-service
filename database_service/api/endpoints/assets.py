from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from loguru import logger

from database_service.api import deps
from database_service.common import utils
from database_service.crud import CRUDAsset, CRUDMetadata
from database_service.schemas import asset, metadata

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=List[metadata.MetadataRead])
def read_asset_metadata(
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(),
):
    """Returns metadata of all assets"""
    return CRUDMetadata(db_model).get_multi(sess)


@router.get("/{ticker}", response_model=metadata.MetadataRead)
def read_asset_metadata(
    ticker: str,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(),
):
    """Returns metadata of the asset with given id"""
    return CRUDMetadata(db_model).get(sess, ticker)


@router.post("/", status_code=201, response_model=metadata.MetadataDB)
def create_asset_metadata(
    *args,
    metadata_in: metadata.MetadataCreate,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends()
):
    """
    Create new metadata
    """
    return CRUDMetadata(db_model).create(sess, obj_in=metadata_in)


@router.get("/price", response_model=List[asset.AssetRead])
def read_asset_price(
    ticker: str,
    *,
    sess: Session = Depends(deps.get_session),
    db_model: deps.asset = Depends(),
    start_date: datetime = utils.get_last_month(),
    end_date: datetime = datetime.utcnow()
):
    db_model = db_model(ticker)
    return CRUDAsset(db_model).get_by_date(
        sess, start_date=start_date, end_date=end_date
    )


@router.post("/price", response_model=asset.AssetRead, status_code=201)
def create_asset_price(
        *,
        asset_in: asset.AssetCreate,
        sess: Session = Depends(deps.get_session),
        db_model: deps.asset = Depends(),
):
    # db_model for assets return AssetFactory.create_asset function, so it needs to be called to return an asset class.
    db_model = db_model(asset_in.ticker)
    logger.info(f"final model: {db_model}")
    return CRUDAsset(db_model).create(sess, obj_in=asset_in)
