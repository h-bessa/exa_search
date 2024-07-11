from sqlmodel import Session

from api.models.user import User
from api.schemas.user import UserCreate

from api.utils.utils import hashed_password


def get_user(db: Session, user_id: int):
    return db.get(User, user_id)


def create_user(db: Session, user: UserCreate):
    password = hashed_password(str.encode(user.password))
    db_user = User(email=user.email, hashed_password=password)
