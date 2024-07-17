from pydantic import BaseModel, EmailStr
from typing import List

from api.schemas.history import History


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class User(UserBase):
    id: int
    history: List[History] = []

    class Config:
        orm_mode = True
