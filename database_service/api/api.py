from fastapi import APIRouter

from database_service.api.endpoints import assets, orders, wallet

api_router = APIRouter(prefix="/{exchange}")
api_router.include_router(assets.router)
api_router.include_router(orders.router)
api_router.include_router(wallet.router)
