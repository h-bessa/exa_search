from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

    history: List["History"] = Relationship(back_populates="user")


from .history import History
