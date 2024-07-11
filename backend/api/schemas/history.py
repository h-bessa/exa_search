from pydantic import BaseModel


class HistoryBase(BaseModel):
    query: str


class History(HistoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True