from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import (
    UserTable, UserFundsTable, UserSocialsTable,
    CavernTable, MinerTable, UserCavernTable, UserMinerTable, 
    UserElderTable, UserMembersTable,
    QuestTable, UserQuestTable
)
from schemas import QuestCreate, UserQuestCreate, QuestStatus

# User CRUD
def create_user(db: Session, telegram_id: str, username: str, referral_code: str) -> UserTable:
    """
    Create a new user and initialize related tables with default values.
    """
    try:
        db_user = UserTable(telegram_id=telegram_id, username=username, referral_code=referral_code)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user  # Return the created user object
    except SQLAlchemyError as e:
        db.rollback()
        raise

def get_user_with_telegram_id(db: Session, telegram_id: str) -> UserTable:
    """
    Retrieve a user by their Telegram ID.
    """
    try:
        return db.query(UserTable).filter(UserTable.telegram_id == telegram_id).first()
    except SQLAlchemyError as e:
        raise

def get_user_with_referral_code(db: Session, referral_code: str) -> UserTable:
    """
    Retrieve a user by their referral code.
    """
    try:
        return db.query(UserTable).filter(UserTable.referral_code == referral_code).first()
    except SQLAlchemyError as e:
        raise

def get_owner_of_referral_code(db: Session, referral_code: str):
    """
    Fetch the elder user's telegram_id and username using the referral code.
    """
    user = db.query(UserTable).filter(UserTable.referral_code == referral_code).first()
    if user:
        return user.telegram_id, user.username
    return None

# User Funds CRUD
def create_user_funds(db: Session, telegram_id: str) -> UserFundsTable:
    """
    Create a new entry in the UserFundsTable for the user.
    """
    try:
        db_funds = UserFundsTable(telegram_id=telegram_id)
        db.add(db_funds)
        db.commit()
        db.refresh(db_funds)
        return db_funds
    except SQLAlchemyError as e:
        db.rollback()
        raise

# User Socials CRUD
def create_user_socials(db: Session, telegram_id: str) -> UserSocialsTable:
    """
    Create a new entry in the UserSocialsTable for the user.
    """
    try:
        db_socials = UserSocialsTable(telegram_id=telegram_id)
        db.add(db_socials)
        db.commit()
        db.refresh(db_socials)
        return db_socials
    except SQLAlchemyError as e:
        db.rollback()
        raise

# User Elder CRUD
def create_user_elder(db: Session, telegram_id: str, elder_telegram_id: str, elder_username: str) -> UserElderTable:
    """
    Create a new entry in the UserElderTable for the user.
    """
    try:
        db_elder = UserElderTable(
            telegram_id=telegram_id,
            elder_telegram_id=elder_telegram_id,
            elder_username=elder_username
        )
        db.add(db_elder)
        db.commit()
        db.refresh(db_elder)
        return db_elder
    except SQLAlchemyError as e:
        db.rollback()
        raise

# User Members CRUD
def create_user_member(db: Session, elder_telegram_id: str, member_telegram_id: str, member_username: str) -> UserMembersTable:
    """
    Create a new entry in the UserMembersTable for the elder user.
    The newly created user is added as a member to the elder user.
    """
    try:
        db_member = UserMembersTable(
            telegram_id=elder_telegram_id,
            member_telegram_id=member_telegram_id,
            member_username=member_username
        )
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member
    except SQLAlchemyError as e:
        db.rollback()
        raise

# User Cavern CRUD
def create_user_caverns(db: Session, telegram_id: str) -> None:
    """
    Create default entries in the UserCavernTable for the user.
    """
    try:
        default_caverns = db.query(CavernTable).all()
        for cavern in default_caverns:
            db_cavern = UserCavernTable(
                telegram_id=telegram_id,
                cavern_id=cavern.id,
                purchased=False
            )
            db.add(db_cavern)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise

# User Miner CRUD
def create_user_miners(db: Session, telegram_id: str) -> None:
    """
    Create default entries in the UserMinerTable for the user.
    """
    try:
        default_miners = db.query(MinerTable).all()
        for miner in default_miners:
            db_miner = UserMinerTable(
                telegram_id=telegram_id,
                miner_id=miner.id,
                level=0
            )
            db.add(db_miner)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise

# Quest CRUD
def create_quest(db: Session, quest: QuestCreate) -> QuestTable:
    """
    Create a new quest in the QuestTable.
    """
    try:
        db_quest = QuestTable(**quest.dict())
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        return db_quest
    except SQLAlchemyError as e:
        db.rollback()
        raise

def get_quest_by_id(db: Session, quest_id: int) -> QuestTable:
    """
    Retrieve a quest by its ID.
    """
    try:
        return db.query(QuestTable).filter(QuestTable.id == quest_id).first()
    except SQLAlchemyError as e:
        raise

def get_all_quests(db: Session) -> list[QuestTable]:
    """
    Retrieve all quests from the QuestTable.
    """
    try:
        return db.query(QuestTable).all()
    except SQLAlchemyError as e:
        raise

# User Quest CRUD
def get_user_quests(db: Session, telegram_id: str) -> list[UserQuestTable]:
    """
    Retrieve all quests for a specific user.
    """
    try:
        return db.query(UserQuestTable).filter(UserQuestTable.telegram_id == telegram_id).all()
    except SQLAlchemyError as e:
        raise

def update_user_quest_status(db: Session, user_quest_id: int, status: QuestStatus) -> UserQuestTable:
    """
    Update the status of a user's quest.
    """
    try:
        db_user_quest = db.query(UserQuestTable).filter(UserQuestTable.id == user_quest_id).first()
        if db_user_quest:
            db_user_quest.status = status
            db.commit()
            db.refresh(db_user_quest)
        return db_user_quest
    except SQLAlchemyError as e:
        db.rollback()
        raise

def create_user_quest(db: Session, user_quest: UserQuestCreate) -> UserQuestTable:
    """
    Create a new entry in the UserQuestTable for the user.
    """
    try:
        db_user_quest = UserQuestTable(**user_quest.dict())
        db.add(db_user_quest)
        db.commit()
        db.refresh(db_user_quest)
        return db_user_quest
    except SQLAlchemyError as e:
        db.rollback()
        raise

def assign_quests_to_user(db: Session, telegram_id: str) -> None:
    """
    Assign all quests from the QuestTable to a user if they don't already have them.
    """
    try:
        existing_quest_ids = (
            db.query(UserQuestTable.quest_id)
            .filter(UserQuestTable.telegram_id == telegram_id)
            .subquery()
        )

        new_quests = (
            db.query(QuestTable)
            .filter(QuestTable.id.notin_(existing_quest_ids))
            .all()
        )

        for quest in new_quests:
            user_quest = UserQuestCreate(telegram_id=telegram_id, quest_id=quest.id)
            create_user_quest(db, user_quest)
    except SQLAlchemyError as e:
        db.rollback()
        raise