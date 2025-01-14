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
    return db_user

def get_user(db: Session, telegram_id: str):
    return db.query(UserTable).filter(UserTable.telegram_id == telegram_id).first()

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

# User Cavern CRUD
def create_user_cavern(db: Session, telegram_id: str, cavern_id: int):
    db_cavern = UserCavernTable(telegram_id=telegram_id, cavern_id=cavern_id)
    db.add(db_cavern)
    db.commit()
    db.refresh(db_cavern)
    return db_cavern

# User Miner CRUD
def create_user_miner(db: Session, telegram_id: str, miner_id: int):
    db_miner = UserMinerTable(telegram_id=telegram_id, miner_id=miner_id)
    db.add(db_miner)
    db.commit()
    db.refresh(db_miner)
    return db_miner

# User Quest CRUD
def create_user_quest(db: Session, telegram_id: str, quest_id: int):
    db_quest = UserQuestTable(telegram_id=telegram_id, quest_id=quest_id)
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

# User Elder CRUD
def create_user_elder(db: Session, telegram_id: str, elder_telegram_id: str, elder_username: str):
    db_elder = UserElderTable(telegram_id=telegram_id, elder_telegram_id=elder_telegram_id, elder_username=elder_username)
    db.add(db_elder)
    db.commit()
    db.refresh(db_elder)
    return db_elder

# User Members CRUD
def create_user_member(db: Session, telegram_id: str, member_telegram_id: str, member_username: str):
    db_member = UserMembersTable(telegram_id=telegram_id, member_telegram_id=member_telegram_id, member_username=member_username)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member