from fastapi import APIRouter, Depends
from backend2.auth.auth_bearer import JWTBearer
from backend2.db.schemas import Items as ItemSchema
from backend2.operations.table import add_item, delete_item, read_items, read_item
from backend2.db.database import SessionLocal
from sqlalchemy.orm import Session

from typing import Annotated


router = APIRouter(
    prefix="/backend2",
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    class Config:
        from_attributes = True

class ItemId(BaseModel):
    id: int
    class Config:
        from_attributes = True

@router.post("/items", tags=["table"], dependencies=[Depends(JWTBearer())])
async def create_item(item: Annotated[Item, {"description": "Items to be added"}], db: Annotated[Session, Depends(get_db)]):
    return add_item(db, ItemSchema(**item.model_dump()))


@router.delete("/items/{item_index}", dependencies=[Depends(JWTBearer())])
async def remove_item(item_index: Annotated[int, {'description": "Item index to be deleted'}], db: Annotated[Session, Depends(get_db)]):
    return delete_item(db, item_index)

@router.get("/items/all")
@router.get("/items/all/")
async def read_all_items(db: Annotated[Session, Depends(get_db)]):
    return read_items(db)

@router.get("/items/{item_id}")
async def read_item_index(item_id: int, db: Annotated[Session, Depends(get_db)]):
    return read_item(db, item_id)