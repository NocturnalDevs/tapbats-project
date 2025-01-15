# database/crud.py
from sqlalchemy.orm import Session
from .models import (
    UserTable, UserFundsTable, UserTapMiningTable, UserSocialsTable,
    UserCavernTable, UserMinerTable, UserElderTable, CavernTable, MinerTable, 
    QuestTable, UserQuestTable
)

from schemas import QuestCreate, UserQuestCreate, QuestStatus  # Import the missing schemas

# User CRUD
def create_user(db: Session, telegram_id: str, username: str, referral_code: str):
    """
    Create a new user and initialize related tables with default values.
    """
    db_user = UserTable(telegram_id=telegram_id, username=username, referral_code=referral_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_with_telegram_id(db: Session, telegram_id: str):
    """
    Retrieve a user by their Telegram ID.
    """
    return db.query(UserTable).filter(UserTable.telegram_id == telegram_id).first()

def get_user_with_referral_code(db: Session, referral_code: str):
    """
    Retrieve a user by their referral code.
    """
    return db.query(UserTable).filter(UserTable.referral_code == referral_code).first()

# User Funds CRUD
def create_user_funds(db: Session, telegram_id: str):
    """
    Create a new entry in the UserFundsTable for the user.
    """
    db_funds = UserFundsTable(telegram_id=telegram_id)
    db.add(db_funds)
    db.commit()
    db.refresh(db_funds)
    return db_funds

# User Tap Mining CRUD
def create_user_tap_mining(db: Session, telegram_id: str):
    """
    Create a new entry in the UserTapMiningTable for the user.
    """
    db_tap_mining = UserTapMiningTable(telegram_id=telegram_id)
    db.add(db_tap_mining)
    db.commit()
    db.refresh(db_tap_mining)
    return db_tap_mining

# User Socials CRUD
def create_user_socials(db: Session, telegram_id: str):
    """
    Create a new entry in the UserSocialsTable for the user.
    """
    db_socials = UserSocialsTable(telegram_id=telegram_id)
    db.add(db_socials)
    db.commit()
    db.refresh(db_socials)
    return db_socials

# User Elder CRUD
def create_user_elder(db: Session, telegram_id: str, elder_telegram_id: str, elder_username: str):
    """
    Create a new entry in the UserElderTable for the user.
    """
    db_elder = UserElderTable(
        telegram_id=telegram_id,
        elder_telegram_id=elder_telegram_id,
        elder_username=elder_username
    )
    db.add(db_elder)
    db.commit()
    db.refresh(db_elder)
    return db_elder

# User Cavern CRUD
def create_user_caverns(db: Session, telegram_id: str):
    """
    Create default entries in the UserCavernTable for the user.
    """
    default_caverns = db.query(CavernTable).all()
    for cavern in default_caverns:
        db_cavern = UserCavernTable(
            telegram_id=telegram_id,
            cavern_id=cavern.id,
            purchased=False
        )
        db.add(db_cavern)
    db.commit()

# User Miner CRUD
def create_user_miners(db: Session, telegram_id: str):
    """
    Create default entries in the UserMinerTable for the user.
    """
    default_miners = db.query(MinerTable).all()
    for miner in default_miners:
        db_miner = UserMinerTable(
            telegram_id=telegram_id,
            miner_id=miner.id,
            level=0
        )
        db.add(db_miner)
    db.commit()

# Quest CRUD
def create_quest(db: Session, quest: QuestCreate):
    """
    Create a new quest in the QuestTable.
    """
    db_quest = QuestTable(**quest.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def get_quest_by_id(db: Session, quest_id: int):
    """
    Retrieve a quest by its ID.
    """
    return db.query(QuestTable).filter(QuestTable.id == quest_id).first()

def get_all_quests(db: Session):
    """
    Retrieve all quests from the QuestTable.
    """
    return db.query(QuestTable).all()

# User Quest CRUD
def create_user_quest(db: Session, user_quest: UserQuestCreate):
    """
    Create a new entry in the UserQuestTable for the user.
    """
    db_user_quest = UserQuestTable(**user_quest.dict())
    db.add(db_user_quest)
    db.commit()
    db.refresh(db_user_quest)
    return db_user_quest

def get_user_quests(db: Session, telegram_id: str):
    """
    Retrieve all quests for a specific user.
    """
    return db.query(UserQuestTable).filter(UserQuestTable.telegram_id == telegram_id).all()

def update_user_quest_status(db: Session, user_quest_id: int, status: QuestStatus):
    """
    Update the status of a user's quest.
    """
    db_user_quest = db.query(UserQuestTable).filter(UserQuestTable.id == user_quest_id).first()
    if db_user_quest:
        db_user_quest.status = status
        db.commit()
        db.refresh(db_user_quest)
    return db_user_quest

def assign_quests_to_user(db: Session, telegram_id: str):
    """
    Assign all quests from the QuestTable to a user if they don't already have them.
    """
    existing_user_quests = get_user_quests(db, telegram_id)
    existing_quest_ids = {uq.quest_id for uq in existing_user_quests}

    all_quests = get_all_quests(db)
    for quest in all_quests:
        if quest.id not in existing_quest_ids:
            user_quest = UserQuestCreate(telegram_id=telegram_id, quest_id=quest.id)
            create_user_quest(db, user_quest)