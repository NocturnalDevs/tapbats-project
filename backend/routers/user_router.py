from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db

from schemas import UserCreateWrapper, SaveUserResponse
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

@router.post("/save-user/", response_model=SaveUserResponse)
def save_user(user_data_wrapper: UserCreateWrapper, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.save_user(user_data_wrapper.user_data)