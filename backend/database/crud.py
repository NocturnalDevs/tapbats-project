# database/crud.py
from sqlalchemy.orm import Session
from .models import (
    UserTable, UserFundsTable, UserTapMiningTable, UserSocialsTable,
    UserCavernTable, UserMinerTable, UserQuestTable, UserElderTable, UserMembersTable
)

# User CRUD
def create_user(db: Session, telegram_id: str, username: str, referral_code: str):
    db_user = UserTable(telegram_id=telegram_id, username=username, referral_code=referral_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Create related tables
    create_user_funds(db, telegram_id)
    create_user_tap_mining(db, telegram_id)
    create_user_socials(db, telegram_id)
    create_user_elder(db, telegram_id, "default_elder_id", "default_elder_username")
    return db_user

# User Funds CRUD
def create_user_funds(db: Session, telegram_id: str):
    db_funds = UserFundsTable(telegram_id=telegram_id)
    db.add(db_funds)
    db.commit()
    db.refresh(db_funds)
    return db_funds

# User Tap Mining CRUD
def create_user_tap_mining(db: Session, telegram_id: str):
    db_tap_mining = UserTapMiningTable(telegram_id=telegram_id)
    db.add(db_tap_mining)
    db.commit()
    db.refresh(db_tap_mining)
    return db_tap_mining

# User Socials CRUD
def create_user_socials(db: Session, telegram_id: str):
    db_socials = UserSocialsTable(telegram_id=telegram_id)
    db.add(db_socials)
    db.commit()
    db.refresh(db_socials)
    return db_socials

# User Elder CRUD
def create_user_elder(db: Session, telegram_id: str, elder_telegram_id: str, elder_username: str):
    db_elder = UserElderTable(telegram_id=telegram_id, elder_telegram_id=elder_telegram_id, elder_username=elder_username)
    db.add(db_elder)
    db.commit()
    db.refresh(db_elder)
    return db_elder