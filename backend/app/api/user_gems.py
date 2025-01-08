from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.user_gems import UserGemsCreate, UserGems
from app.database.crud.user_gems import get_user_gems, create_user_gems, update_user_gems

router = APIRouter()

@router.post("/user_gems/", response_model=UserGems)
def create_user_gems_endpoint(user_gems: UserGemsCreate, db: Session = Depends(get_db)):
    return create_user_gems(db, user_gems)

@router.get("/user_gems/{telegram_id}", response_model=UserGems)
def read_user_gems(telegram_id: str, db: Session = Depends(get_db)):
    user_gems = get_user_gems(db, telegram_id)
    if not user_gems:
        raise HTTPException(status_code=404, detail="User gems not found")
    return user_gems

@router.post("/user_gems/{telegram_id}/mine")
def mine_gems(telegram_id: str, gem_count: float, db: Session = Depends(get_db)):
    user_gems = update_user_gems(db, telegram_id, gem_count)
    if not user_gems:
        raise HTTPException(status_code=404, detail="User gems not found")
    return user_gems