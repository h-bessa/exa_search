from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class History(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    query: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="history")


from .user import User
