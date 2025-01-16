from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas import UserCreate, User
from services.user_service import UserService

router = APIRouter()

@router.get("/user-exists/{telegram_id}", response_model=dict)
def check_user_exists(telegram_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.check_user_exists(telegram_id)

@router.get("/validate-referral-code/{referral_code}", response_model=dict)
def validate_referral_code(referral_code: str, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.validate_referral_code(referral_code)

@router.post("/save-user/", response_model=User)
def save_user(user: UserCreate, inputted_referral_code: str, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.save_user(user, inputted_referral_code)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))