from sqlalchemy import Column, Integer, String

from backend2.db.database import Base

class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(String(50), unique=True)
