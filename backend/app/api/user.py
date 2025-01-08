from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.user import UserCreate, User
from app.database.crud.user import get_user, create_user, update_user_last_online

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/{telegram_id}", response_model=User)
def read_user(telegram_id: str, db: Session = Depends(get_db)):
    user = get_user(db, telegram_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{telegram_id}/last_online")
def update_last_online(telegram_id: str, last_online: str, db: Session = Depends(get_db)):
    user = update_user_last_online(db, telegram_id, last_online)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user