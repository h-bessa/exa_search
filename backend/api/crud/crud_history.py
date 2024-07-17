from sqlmodel import Session, select

from api.models.history import History
from api.schemas.history import HistoryBase
from api.schemas.user import UserCreate


def get_history_by_user_id(db: Session, user_id: int):
    return db.exec(select(History).where(History.user_id == user_id)).first()


def create_history(db: Session, user_id: UserCreate, query: HistoryBase):
    print("user_id YOOOOOOOOO", user_id)
    print("query YAAAAAAAAAA", query)

    db_history = History(query=query)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history
