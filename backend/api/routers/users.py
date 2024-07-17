from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from api import crud
from api.database import get_session
from api.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post('/users/', response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    user_created = crud.create_user(db, user=user)
    if user is None:
        raise HTTPException(status_code=404, detail="User can not be empty")
    return user_created
