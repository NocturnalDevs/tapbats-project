from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, models
from ..database.connection import get_db
from ..schemas import UserCreate, User, UserFundsCreate, UserFunds, UserTapMiningCreate, UserTapMining

router = APIRouter()

# Endpoint to check if a user exists
@router.get("/user-exists/{telegram_id}", response_model=dict)
def check_user_exists(telegram_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, telegram_id=str(telegram_id))
    return {"exists": db_user is not None}

# Endpoint to validate a referral code
@router.get("/validate-referral-code/{referral_code}", response_model=dict)
def validate_referral_code(referral_code: str, db: Session = Depends(get_db)):
    db_user = db.query(models.UserTable).filter(models.UserTable.referral_code == referral_code).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Referral code not found")
    return {"valid": True}

# Endpoint to save a new user
@router.post("/save-user/", response_model=User)
def save_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    db_user = crud.get_user(db, telegram_id=user.telegram_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Create the user
    new_user = crud.create_user(db, telegram_id=user.telegram_id, username=user.username, referral_code=user.referral_code)
    return new_user

# Endpoint to get user details
@router.get("/users/{telegram_id}", response_model=User)
def get_user(telegram_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Endpoint to create user funds
@router.post("/users/{telegram_id}/funds", response_model=UserFunds)
def create_user_funds(telegram_id: str, funds: UserFundsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_funds = crud.create_user_funds(db, telegram_id=telegram_id)
    return db_funds

# Endpoint to create user tap mining
@router.post("/users/{telegram_id}/tap-mining", response_model=UserTapMining)
def create_user_tap_mining(telegram_id: str, tap_mining: UserTapMiningCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_tap_mining = crud.create_user_tap_mining(db, telegram_id=telegram_id)
    return db_tap_mining