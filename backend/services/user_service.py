from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import crud, models
from schemas import UserCreate, User
from utils.generate_referral_code import generate_referral_code

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def check_user_exists(self, telegram_id: int) -> dict:
        db_user = crud.get_user_with_telegram_id(self.db, telegram_id=str(telegram_id))
        return {"exists": db_user is not None}

    def validate_referral_code(self, referral_code: str) -> dict:
        db_user = crud.get_user_with_referral_code(self.db, referral_code=referral_code)
        return {"valid": db_user is not None}

    def is_referral_code_unique(self, referral_code: str) -> bool:
        return crud.get_user_with_referral_code(self.db, referral_code=str(referral_code)) is None

    def save_user(self, user: UserCreate, inputted_referral_code: str) -> User:
        try:
            # Step 1: Check if the user already exists
            existing_user = crud.get_user_with_telegram_id(self.db, telegram_id=user.telegram_id)
            if existing_user:
                return existing_user  # Return the existing user instead of raising an error

            # Step 2: Fetch the telegram ID and username of the owner of the referral code (elder)
            elder_user = self.db.query(models.UserTable.telegram_id, models.UserTable.username) \
                    .filter(models.UserTable.referral_code == inputted_referral_code) \
                    .first()

            if elder_user:
                code_owner_telegram_id = elder_user.telegram_id
                code_owner_username = elder_user.username
            else:
                code_owner_telegram_id = None
                code_owner_username = None

            # Step 3: Generate a new referral code for the new user
            new_referral_code = generate_referral_code()
            while not self.is_referral_code_unique(new_referral_code):  # Ensure the code is unique
                new_referral_code = generate_referral_code()

            # Step 4: Save the new user with their own referral code
            new_user = crud.create_user(
                self.db,
                telegram_id=user.telegram_id,
                username=user.username,
                referral_code=new_referral_code
            )

            # Step 5: Create related entries for the new user
            crud.create_user_funds(self.db, telegram_id=user.telegram_id)
            crud.create_user_tap_mining(self.db, telegram_id=user.telegram_id)
            crud.create_user_socials(self.db, telegram_id=user.telegram_id)
            crud.create_user_caverns(self.db, telegram_id=user.telegram_id)
            crud.create_user_miners(self.db, telegram_id=user.telegram_id)
            crud.assign_quests_to_user(self.db, telegram_id=user.telegram_id)

            # Step 6: Create UserElderTable entry if elder user exists
            if code_owner_telegram_id and code_owner_username:
                crud.create_user_elder(
                    self.db,
                    telegram_id=user.telegram_id,
                    elder_telegram_id=code_owner_telegram_id,
                    elder_username=code_owner_username
                )

            # Commit the transaction
            self.db.commit()

            # Refresh the new_user instance to include the related data
            self.db.refresh(new_user)
            return new_user

        except IntegrityError as e:
            self.db.rollback()
            raise ValueError("User already exists or referral code is not unique")

        except Exception as e:
            self.db.rollback()
            raise ValueError(f"Error saving user: {str(e)}")