from sqlmodel import Session, select

from api.models.user import User
from api.schemas.user import UserCreate

from api.utils.utils import hashed_password


def get_user(db: Session, user_id: int):
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).where(User.email == email)).first()


def create_user(db: Session, user: UserCreate):
    print("user YOOOOOOOOO", user)
    password = hashed_password(str.encode(user.password))
    print("user YAAAAAAAAAA", password)

    db_user = User(email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
