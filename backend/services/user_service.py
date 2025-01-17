from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import crud, models
from schemas import UserCreate, User
from fastapi import HTTPException
from utils.generate_referral_code import generate_referral_code

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def check_user_exists(self, telegram_id: int) -> dict:
        db_user = crud.get_user_with_telegram_id(self.db, telegram_id=str(telegram_id))
        return {"exists": db_user is not None}

    def validate_referral_code(self, referral_code: str) -> dict:
        db_user = crud.get_user_with_referral_code(self.db, referral_code=str(referral_code))
        return {"valid": db_user is not None}

    def is_referral_code_unique(self, referral_code: str) -> bool:
        return crud.get_user_with_referral_code(self.db, referral_code=str(referral_code)) is None

    def save_user(self, new_user: UserCreate) -> dict:
        # Initialize a dictionary to track table creation status
        table_status = {}

        try:
            # Step 1: Generate a new referral code for the new user
            newly_generated_referral_code = generate_referral_code()
            while not self.is_referral_code_unique(newly_generated_referral_code):  # Ensure the code is unique
                newly_generated_referral_code = generate_referral_code()

            # Preserve the elder referral code before overwriting
            elder_referral_code = new_user.elder_referral_code

            # Step 2: Save the new user with their own referral code
            new_user = crud.create_user(
                self.db,
                telegram_id=new_user.telegram_id,
                username=new_user.username,
                referral_code=newly_generated_referral_code  # Overwrites the referral code
            )
            table_status["UserTable"] = "success"

            # Step 3: Create related entries for the new user
            crud.create_user_funds(self.db, telegram_id=new_user.telegram_id)
            table_status["UserFundsTable"] = "success"

            crud.create_user_socials(self.db, telegram_id=new_user.telegram_id)
            table_status["UserSocialsTable"] = "success"

            crud.create_user_caverns(self.db, telegram_id=new_user.telegram_id)
            table_status["UserCavernsTable"] = "success"

            crud.create_user_miners(self.db, telegram_id=new_user.telegram_id)
            table_status["UserMinersTable"] = "success"

            crud.assign_quests_to_user(self.db, telegram_id=new_user.telegram_id)
            table_status["UserQuestsTable"] = "success"

            # Step 4: Fetch the elder user using the preserved elder_referral_code
            elder_user = crud.get_owner_of_referral_code(self.db, referral_code=elder_referral_code)
            if not elder_user:
                raise HTTPException(status_code=400, detail="Invalid elder referral code")

            # Extract telegram_id and username from the returned tuple
            elder_telegram_id, elder_username = elder_user

            # Step 5: Create elder entry for the new user
            crud.create_user_elder(
                self.db,
                telegram_id=new_user.telegram_id,
                elder_telegram_id=elder_telegram_id,
                elder_username=elder_username
            )
            table_status["UserElderTable"] = "success"

            # Step 6: Add the new user as a member of the elder
            crud.create_user_member(
                self.db,
                elder_telegram_id=elder_telegram_id,
                member_telegram_id=new_user.telegram_id,
                member_username=new_user.username
            )
            table_status["UserMembersTable"] = "success"

            # Commit the transaction
            self.db.commit()

            # Refresh the new_user instance to include the related data
            self.db.refresh(new_user)

            # Return the table creation status
            return {"tables": table_status}

        except Exception as e:
            # Rollback the transaction in case of an error
            self.db.rollback()

            # Update the table status for any tables that failed
            for table in ["UserTable", "UserFundsTable", "UserSocialsTable", "UserCavernsTable", "UserMinersTable", "UserQuestsTable", "UserElderTable", "UserMembersTable"]:
                if table not in table_status:
                    table_status[table] = "failure"

            # Return the table creation status with the error
            return {"tables": table_status, "error": str(e)}