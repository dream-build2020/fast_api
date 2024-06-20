from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class Mysql(BaseModel):
    ID: int
    User_ID: int
    User: str
