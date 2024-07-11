from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from api import crud
from api.database import get_session
from api.models.user import User

router = APIRouter()


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

def create_user(db: Session = Depends(get_session)):
    db_user = crud.create_user
