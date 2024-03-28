from typing import Optional
from pydantic import BaseModel, validator


class CreatePotion(BaseModel):
    name: str
    cost: int


class ShowPotion(BaseModel):
    id: int
    name: str
    cost: int
    seller_id: int
    is_active: bool

    class Config():
        orm_mode = True


class UpdatePotion(BaseModel):
    name: str
    cost: int
    is_active: bool

