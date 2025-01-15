from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import (
    UserTable, UserFundsTable, UserTapMiningTable, UserSocialsTable,
    UserCavernTable, UserMinerTable, UserElderTable, CavernTable, MinerTable,
    QuestTable, UserQuestTable
)
from schemas import QuestCreate, UserQuestCreate, QuestStatus
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# User CRUD
def create_user(db: Session, telegram_id: str, username: str, referral_code: str) -> UserTable:
    """
    Create a new user and initialize related tables with default values.
    """
    logger.debug(f"Creating user with telegram_id={telegram_id}, username={username}")
    try:
        # Check if the user already exists
        db_user = get_user_with_telegram_id(db, telegram_id)
        if db_user:
            logger.warning(f"User with telegram_id={telegram_id} already exists")
            return db_user  # Return the existing user instead of raising an error

        # Create a new user
        db_user = UserTable(telegram_id=telegram_id, username=username, referral_code=referral_code)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.debug(f"User created successfully: {db_user}")
        return db_user
    except SQLAlchemyError as e:
        logger.error(f"Error creating user: {str(e)}")
        db.rollback()
        raise

def get_user_with_telegram_id(db: Session, telegram_id: str) -> UserTable:
    """
    Retrieve a user by their Telegram ID.
    """
    logger.debug(f"Fetching user with telegram_id={telegram_id}")
    try:
        return db.query(UserTable).filter(UserTable.telegram_id == telegram_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching user: {str(e)}")
        raise

def get_user_with_referral_code(db: Session, referral_code: str) -> UserTable:
    """
    Retrieve a user by their referral code.
    """
    logger.debug(f"Fetching user with referral_code={referral_code}")
    try:
        return db.query(UserTable).filter(UserTable.referral_code == referral_code).first()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching user: {str(e)}")
        raise

# User Funds CRUD
def create_user_funds(db: Session, telegram_id: str) -> UserFundsTable:
    """
    Create a new entry in the UserFundsTable for the user.
    """
    logger.debug(f"Creating user funds for telegram_id={telegram_id}")
    try:
        db_funds = UserFundsTable(telegram_id=telegram_id)
        db.add(db_funds)
        db.commit()
        db.refresh(db_funds)
        logger.debug(f"User funds created successfully: {db_funds}")
        return db_funds
    except SQLAlchemyError as e:
        logger.error(f"Error creating user funds: {str(e)}")
        db.rollback()
        raise

# User Tap Mining CRUD
def create_user_tap_mining(db: Session, telegram_id: str) -> UserTapMiningTable:
    """
    Create a new entry in the UserTapMiningTable for the user.
    """
    logger.debug(f"Creating user tap mining for telegram_id={telegram_id}")
    try:
        db_tap_mining = UserTapMiningTable(telegram_id=telegram_id)
        db.add(db_tap_mining)
        db.commit()
        db.refresh(db_tap_mining)
        logger.debug(f"User tap mining created successfully: {db_tap_mining}")
        return db_tap_mining
    except SQLAlchemyError as e:
        logger.error(f"Error creating user tap mining: {str(e)}")
        db.rollback()
        raise

# User Socials CRUD
def create_user_socials(db: Session, telegram_id: str) -> UserSocialsTable:
    """
    Create a new entry in the UserSocialsTable for the user.
    """
    logger.debug(f"Creating user socials for telegram_id={telegram_id}")
    try:
        db_socials = UserSocialsTable(telegram_id=telegram_id)
        db.add(db_socials)
        db.commit()
        db.refresh(db_socials)
        logger.debug(f"User socials created successfully: {db_socials}")
        return db_socials
    except SQLAlchemyError as e:
        logger.error(f"Error creating user socials: {str(e)}")
        db.rollback()
        raise

# User Elder CRUD
def create_user_elder(db: Session, telegram_id: str, elder_telegram_id: str, elder_username: str) -> UserElderTable:
    """
    Create a new entry in the UserElderTable for the user.
    """
    logger.debug(f"Creating user elder for telegram_id={telegram_id}, elder_telegram_id={elder_telegram_id}")
    try:
        db_elder = UserElderTable(
            telegram_id=telegram_id,
            elder_telegram_id=elder_telegram_id,
            elder_username=elder_username
        )
        db.add(db_elder)
        db.commit()
        db.refresh(db_elder)
        logger.debug(f"User elder created successfully: {db_elder}")
        return db_elder
    except SQLAlchemyError as e:
        logger.error(f"Error creating user elder: {str(e)}")
        db.rollback()
        raise

# User Cavern CRUD
def create_user_caverns(db: Session, telegram_id: str) -> None:
    """
    Create default entries in the UserCavernTable for the user.
    """
    logger.debug(f"Creating user caverns for telegram_id={telegram_id}")
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
        logger.debug(f"User caverns created successfully for telegram_id={telegram_id}")
    except SQLAlchemyError as e:
        logger.error(f"Error creating user caverns: {str(e)}")
        db.rollback()
        raise

# User Miner CRUD
def create_user_miners(db: Session, telegram_id: str) -> None:
    """
    Create default entries in the UserMinerTable for the user.
    """
    logger.debug(f"Creating user miners for telegram_id={telegram_id}")
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
        logger.debug(f"User miners created successfully for telegram_id={telegram_id}")
    except SQLAlchemyError as e:
        logger.error(f"Error creating user miners: {str(e)}")
        db.rollback()
        raise

# Quest CRUD
def create_quest(db: Session, quest: QuestCreate) -> QuestTable:
    """
    Create a new quest in the QuestTable.
    """
    logger.debug(f"Creating quest: {quest}")
    try:
        db_quest = QuestTable(**quest.dict())
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        logger.debug(f"Quest created successfully: {db_quest}")
        return db_quest
    except SQLAlchemyError as e:
        logger.error(f"Error creating quest: {str(e)}")
        db.rollback()
        raise

def get_quest_by_id(db: Session, quest_id: int) -> QuestTable:
    """
    Retrieve a quest by its ID.
    """
    logger.debug(f"Fetching quest with id={quest_id}")
    try:
        return db.query(QuestTable).filter(QuestTable.id == quest_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching quest: {str(e)}")
        raise

def get_all_quests(db: Session) -> list[QuestTable]:
    """
    Retrieve all quests from the QuestTable.
    """
    logger.debug("Fetching all quests")
    try:
        return db.query(QuestTable).all()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching quests: {str(e)}")
        raise

# User Quest CRUD
def create_user_quest(db: Session, user_quest: UserQuestCreate) -> UserQuestTable:
    """
    Create a new entry in the UserQuestTable for the user.
    """
    logger.debug(f"Creating user quest: {user_quest}")
    try:
        db_user_quest = UserQuestTable(**user_quest.dict())
        db.add(db_user_quest)
        db.commit()
        db.refresh(db_user_quest)
        logger.debug(f"User quest created successfully: {db_user_quest}")
        return db_user_quest
    except SQLAlchemyError as e:
        logger.error(f"Error creating user quest: {str(e)}")
        db.rollback()
        raise

def get_user_quests(db: Session, telegram_id: str) -> list[UserQuestTable]:
    """
    Retrieve all quests for a specific user.
    """
    logger.debug(f"Fetching user quests for telegram_id={telegram_id}")
    try:
        return db.query(UserQuestTable).filter(UserQuestTable.telegram_id == telegram_id).all()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching user quests: {str(e)}")
        raise

def update_user_quest_status(db: Session, user_quest_id: int, status: QuestStatus) -> UserQuestTable:
    """
    Update the status of a user's quest.
    """
    logger.debug(f"Updating user quest status for id={user_quest_id} to {status}")
    try:
        db_user_quest = db.query(UserQuestTable).filter(UserQuestTable.id == user_quest_id).first()
        if db_user_quest:
            db_user_quest.status = status
            db.commit()
            db.refresh(db_user_quest)
            logger.debug(f"User quest status updated successfully: {db_user_quest}")
        return db_user_quest
    except SQLAlchemyError as e:
        logger.error(f"Error updating user quest status: {str(e)}")
        db.rollback()
        raise

def assign_quests_to_user(db: Session, telegram_id: str) -> None:
    """
    Assign all quests from the QuestTable to a user if they don't already have them.
    """
    logger.debug(f"Assigning quests to user with telegram_id={telegram_id}")
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
        logger.debug(f"Quests assigned successfully to user with telegram_id={telegram_id}")
    except SQLAlchemyError as e:
        logger.error(f"Error assigning quests to user: {str(e)}")
        db.rollback()
        raise