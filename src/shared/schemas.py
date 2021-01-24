# this file is called schemas to avoid confusion with sqlalchemy and pydantic both overloading the term model
# it's also sort of a clever name because it is enforcing a "type-schema" of sorts on the models (is this right?)

from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    # orm_mode allows mapping these pydantic models to sqlalchemy classes
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True