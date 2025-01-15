# routers/user_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import crud, models
from database.connection import get_db
from schemas import UserCreate, User
from utils.generate_referral_code import generate_referral_code

router = APIRouter()

# Endpoint to check if a user exists
@router.get("/user-exists/{telegram_id}", response_model=dict)
def check_user_exists(telegram_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_with_telegram_id(db, telegram_id=str(telegram_id))
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist")
    return {"exists": db_user is not None}

@router.get("/validate-referral-code/{referral_code}", response_model=dict)
def validate_referral_code(referral_code: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_with_referral_code(db, referral_code=referral_code)
    if not db_user:
        raise HTTPException(status_code=404, detail="Referral code not found")
    return {"valid": True}

# Endpoint to save a new user
def is_referral_code_unique(db: Session, referral_code: str) -> bool:
    """Check if the referral code is unique in the database."""
    return crud.get_user_with_referral_code(db, referral_code=str(referral_code)) is None

@router.post("/save-user/", response_model=User)
def save_user(user: UserCreate, inputted_referral_code: str, db: Session = Depends(get_db)):
    # Step 1: Fetch the telegram ID and username of the owner - of the referral code (elder) - that the new user sent on the referral input
    elder_user = db.query(models.UserTable.telegram_id, models.UserTable.username) \
            .filter(models.UserTable.referral_code == inputted_referral_code) \
            .first()

    if elder_user:
        code_owner_telegram_id = elder_user.telegram_id
        code_owner_username = elder_user.username
    else:
        # Handle the case where no user is found with the given referral code
        code_owner_telegram_id = None
        code_owner_username = None
    
    # Step 2: Generate a new referral code for the new user
    new_referral_code = generate_referral_code() # imported function from utils
    while not is_referral_code_unique(db, new_referral_code):  # Ensure the code is unique
        new_referral_code = generate_referral_code()

    # Step 3: Save the new user with their own referral code
    new_user = crud.create_user(
        db,
        telegram_id=user.telegram_id,
        username=user.username,
        referral_code=new_referral_code
    )

    # Step 4: Create related entries for the new user
    crud.create_user_funds(db, telegram_id=user.telegram_id)
    crud.create_user_tap_mining(db, telegram_id=user.telegram_id)
    crud.create_user_socials(db, telegram_id=user.telegram_id)
    crud.create_user_caverns(db, telegram_id=user.telegram_id)
    crud.create_user_miners(db, telegram_id=user.telegram_id)
    crud.assign_quests_to_user(db, telegram_id=user.telegram_id)

    # Step 5: Create UserElderTable entry if elder user exists
    if code_owner_telegram_id and code_owner_username:
        crud.create_user_elder(
            db,
            telegram_id=user.telegram_id,
            elder_telegram_id=code_owner_telegram_id,
            elder_username=code_owner_username
        )

    # Refresh the new_user instance to include the related data
    db.refresh(new_user)
    return new_user
