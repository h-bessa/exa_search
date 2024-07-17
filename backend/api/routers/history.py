from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from api import crud
from api.database import get_session
from api.models.history import History
from api.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.get("/history/{user_id}", response_model=History)
def read_history(user_id: int, db: Session = Depends(get_session)):
    db_user_history = crud.get_history_by_user_id(db, user_id=user_id)
    if db_user_history is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user_history
