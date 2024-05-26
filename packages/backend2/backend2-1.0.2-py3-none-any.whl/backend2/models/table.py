from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    class Config:
        from_attributes = True
