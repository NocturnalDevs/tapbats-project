from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import crud, models
from database.connection import get_db
from schemas import UserCreate, User
from utils.generate_referral_code import generate_referral_code
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Endpoint to check if a user exists
@router.get("/user-exists/{telegram_id}", response_model=dict)
def check_user_exists(telegram_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Checking if user with telegram_id={telegram_id} exists")
    try:
        logger.debug(f"Fetching user from database with telegram_id={telegram_id}")
        db_user = crud.get_user_with_telegram_id(db, telegram_id=str(telegram_id))
        if not db_user:
            logger.warning(f"User with telegram_id={telegram_id} does not exist")
            raise HTTPException(status_code=404, detail="User does not exist")
        logger.debug(f"User with telegram_id={telegram_id} exists: {db_user is not None}")
        return {"exists": db_user is not None}
    except Exception as e:
        logger.error(f"Error checking user existence: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error checking user existence: {str(e)}")
    finally:
        db.close()

# Endpoint to validate a referral code
@router.get("/validate-referral-code/{referral_code}", response_model=dict)
def validate_referral_code(referral_code: str, db: Session = Depends(get_db)):
    logger.debug(f"Validating referral code: {referral_code}")
    try:
        db_user = crud.get_user_with_referral_code(db, referral_code=referral_code)
        if not db_user:
            logger.warning(f"Referral code {referral_code} not found")
            raise HTTPException(status_code=404, detail="Referral code not found")
        logger.debug(f"Referral code {referral_code} is valid")
        return {"valid": True}
    except Exception as e:
        logger.error(f"Error validating referral code: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error validating referral code: {str(e)}")
    finally:
        db.close()

# Helper function to check if a referral code is unique
def is_referral_code_unique(db: Session, referral_code: str) -> bool:
    """Check if the referral code is unique in the database."""
    logger.debug(f"Checking if referral code {referral_code} is unique")
    return crud.get_user_with_referral_code(db, referral_code=str(referral_code)) is None

# Endpoint to save a new user
@router.post("/save-user/", response_model=User)
def save_user(user: UserCreate, inputted_referral_code: str, db: Session = Depends(get_db)):
    logger.debug(f"Saving new user with telegram_id={user.telegram_id}")
    try:
        # Step 1: Fetch the telegram ID and username of the owner of the referral code (elder)
        logger.debug(f"Fetching elder user with referral code: {inputted_referral_code}")
        elder_user = db.query(models.UserTable.telegram_id, models.UserTable.username) \
                .filter(models.UserTable.referral_code == inputted_referral_code) \
                .first()

        if elder_user:
            code_owner_telegram_id = elder_user.telegram_id
            code_owner_username = elder_user.username
            logger.debug(f"Elder user found: telegram_id={code_owner_telegram_id}, username={code_owner_username}")
        else:
            # Handle the case where no user is found with the given referral code
            code_owner_telegram_id = None
            code_owner_username = None
            logger.warning(f"No elder user found with referral code: {inputted_referral_code}")

        # Step 2: Generate a new referral code for the new user
        new_referral_code = generate_referral_code()  # Imported function from utils
        logger.debug(f"Generated new referral code: {new_referral_code}")
        while not is_referral_code_unique(db, new_referral_code):  # Ensure the code is unique
            new_referral_code = generate_referral_code()
            logger.debug(f"Generated unique referral code: {new_referral_code}")

        # Step 3: Save the new user with their own referral code
        logger.debug(f"Creating new user with telegram_id={user.telegram_id}, username={user.username}, referral_code={new_referral_code}")
        new_user = crud.create_user(
            db,
            telegram_id=user.telegram_id,
            username=user.username,
            referral_code=new_referral_code
        )

        # Step 4: Create related entries for the new user
        logger.debug(f"Creating related entries for user with telegram_id={user.telegram_id}")
        crud.create_user_funds(db, telegram_id=user.telegram_id)
        crud.create_user_tap_mining(db, telegram_id=user.telegram_id)
        crud.create_user_socials(db, telegram_id=user.telegram_id)
        crud.create_user_caverns(db, telegram_id=user.telegram_id)
        crud.create_user_miners(db, telegram_id=user.telegram_id)
        crud.assign_quests_to_user(db, telegram_id=user.telegram_id)

        # Step 5: Create UserElderTable entry if elder user exists
        if code_owner_telegram_id and code_owner_username:
            logger.debug(f"Creating UserElder entry for user with telegram_id={user.telegram_id}")
            crud.create_user_elder(
                db,
                telegram_id=user.telegram_id,
                elder_telegram_id=code_owner_telegram_id,
                elder_username=code_owner_username
            )

        # Commit the transaction
        db.commit()
        logger.debug(f"User with telegram_id={user.telegram_id} saved successfully")

        # Refresh the new_user instance to include the related data
        db.refresh(new_user)
        return new_user

    except Exception as e:
        # Rollback the transaction in case of an error
        db.rollback()
        logger.error(f"Error saving user: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")

    finally:
        # Close the session
        db.close()