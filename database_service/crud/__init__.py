from .crud_asset import CRUDAsset
from .crud_metadata import CRUDMetadata
from .crud_order import CRUDOrder
from .crud_wallet import CRUDWallet

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
