from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.user_socials import UserSocialsCreate, UserSocials
from app.database.crud.user_socials import get_user_socials, create_user_socials, update_user_socials

router = APIRouter()

@router.post("/user_socials/", response_model=UserSocials)
def create_user_socials_endpoint(user_socials: UserSocialsCreate, db: Session = Depends(get_db)):
    return create_user_socials(db, user_socials)

@router.get("/user_socials/{telegram_id}", response_model=UserSocials)
def read_user_socials(telegram_id: str, db: Session = Depends(get_db)):
    user_socials = get_user_socials(db, telegram_id)
    if not user_socials:
        raise HTTPException(status_code=404, detail="User socials not found")
    return user_socials

@router.put("/user_socials/{telegram_id}")
def update_socials(telegram_id: str, socials_data: dict, db: Session = Depends(get_db)):
    user_socials = update_user_socials(db, telegram_id, socials_data)
    if not user_socials:
        raise HTTPException(status_code=404, detail="User socials not found")
    return user_socials