from sqlalchemy.orm import Session

from backend2.db import schemas


def add_item(db: Session, item: schemas.Items):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_index: int):
    item = db.query(schemas.Items).filter_by(id=item_index).first()
    if item:
        db.delete(item)
        db.commit()
    return item

def read_items(db:Session):
    items = db.query(schemas.Items).all()
    return items

def read_item(db:Session, item_index: int):
    item = db.query(schemas.Items).filter_by(id=item_index).first()
    return item