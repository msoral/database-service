from fastapi import APIRouter

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("/cost")
def read_cost():
    pass


@router.get("/")
def read_portfolio():
    pass
