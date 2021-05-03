from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_service import crud, models, schemas
from database_service.api import deps
from database_service.common import utils

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=List[schemas.MetadataRead])
def read_asset_metadata(
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(deps.metadata),
):
    """Returns metadata of all assets"""
    return crud.CRUDMetadata(db_model).get_multi(sess)


@router.get("/{asset_id}", response_model=schemas.MetadataRead)
def read_asset_metadata(
    asset_id: int,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(deps.metadata),
):
    """Returns metadata of the asset with given id"""
    return crud.CRUDMetadata(db_model).get(sess, asset_id)


@router.post("/", status_code=201, response_model=schemas.MetadataDB)
def create_asset_metadata(
    *,
    metadata_in: schemas.MetadataCreate,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(deps.metadata)
):
    """
    Create new metadata
    """
    metadata = crud.CRUDMetadata(db_model).create(sess, obj_in=metadata_in)
    return metadata


@router.get("/price", response_model=List[schemas.Asset])
def read_asset_price(
    asset_id: int,
    *,
    sess: Session = Depends(deps.get_session),
    db_model: deps.metadata = Depends(deps.asset),
    start_date: datetime = utils.get_last_month(),
    end_date: datetime = datetime.utcnow()
):
    return crud.CRUDAsset(db_model).get_by_date(
        sess, asset_id, start_date=start_date, end_date=end_date
    )


@router.post("/price", response_model=schemas.Asset, status_code=201)
def create_asset_price(
        *,
        asset_in: schemas.Asset,
        sess: Session = Depends(deps.get_session),
        db_model: deps.metadata = Depends(deps.asset),
):
    asset = crud.CRUDAsset(db_model).create(sess, obj_in=asset_in)
    return asset


@router.get("/indicators")
def read_asset_indicators(
        asset_id: int,
        *,
        sess: Session = Depends(deps.get_session),
        db_model: deps.metadata = Depends(deps.asset),
        start_date: datetime = utils.get_last_month(),
        end_date: datetime = datetime.utcnow()
):
    pass
