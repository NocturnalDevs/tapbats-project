from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import database
from app.schemas import user

router = APIRouter()

@router.post("/users/", response_model=user.User)
def create_user(user_create: user.UserCreate, db: Session = Depends(database.get_db)):
    db_user = database.crud.get_user(db, telegramID=user_create.telegramID)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return database.crud.create_user(db, telegramID=user_create.telegramID)

@router.get("/users/{telegramID}", response_model=user.User)
def read_user(telegramID: str, db: Session = Depends(database.get_db)):
    db_user = database.crud.get_user(db, telegramID=telegramID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user