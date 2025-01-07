import random
import string
from sqlalchemy.orm import Session
from datetime import datetime
from . import models

def generate_referral_code(length: int = 8) -> str:
    """Generate a random referral code."""
    characters = string.ascii_letters + string.digits  # Alphanumeric characters
    return ''.join(random.choice(characters) for _ in range(length))

def is_referral_code_unique(db: Session, referral_code: str) -> bool:
    """Check if the referral code is unique."""
    return db.query(models.User).filter(models.User.referralCode == referral_code).first() is None

# ===================== User CRUD Operations =====================
def get_user(db: Session, telegramID: str):
    """Get a user by their Telegram ID."""
    return db.query(models.User).filter(models.User.telegramID == telegramID).first()

def create_user(db: Session, telegramID: str):
    """Create a new user with default values and a unique referral code."""
    # Generate a unique referral code
    referral_code = generate_referral_code()
    while not is_referral_code_unique(db, referral_code):
        referral_code = generate_referral_code()

    # Create the user
    db_user = models.User(
        telegramID=telegramID,
        referralCode=referral_code,
        lastOnline=datetime.utcnow()  # Set lastOnline to the current time
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_last_online(db: Session, telegramID: str, lastOnline: datetime):
    """Update the last online timestamp for a user."""
    db_user = db.query(models.User).filter(models.User.telegramID == telegramID).first()
    if db_user:
        db_user.lastOnline = lastOnline
        db.commit()
        db.refresh(db_user)
    return db_user

# ===================== UserGems CRUD Operations =====================
def get_user_gems(db: Session, telegramID: str):
    """Get a user's gem data."""
    return db.query(models.UserGems).filter(models.UserGems.telegramID == telegramID).first()

def create_user_gems(db: Session, telegramID: str):
    """Create a new user's gem data with default values."""
    db_gems = models.UserGems(telegramID=telegramID)
    db.add(db_gems)
    db.commit()
    db.refresh(db_gems)
    return db_gems

def update_user_gems(db: Session, telegramID: str, totalGemCount: float, availableGemsToMine: float, dailyGemsMined: float):
    """Update a user's gem data."""
    db_gems = db.query(models.UserGems).filter(models.UserGems.telegramID == telegramID).first()
    if db_gems:
        db_gems.totalGemCount = totalGemCount
        db_gems.availableGemsToMine = availableGemsToMine
        db_gems.dailyGemsMined = dailyGemsMined
        db.commit()
        db.refresh(db_gems)
    return db_gems

def update_highest_total_gems(db: Session, telegramID: str, highestTotalGems: float):
    """Update a user's highest total gem count."""
    db_gems = db.query(models.UserGems).filter(models.UserGems.telegramID == telegramID).first()
    if db_gems:
        db_gems.highestTotalGems = highestTotalGems
        db.commit()
        db.refresh(db_gems)
    return db_gems

# ===================== UserSocials CRUD Operations =====================
def get_user_socials(db: Session, telegramID: str):
    """Get a user's social media data."""
    return db.query(models.UserSocials).filter(models.UserSocials.telegramID == telegramID).first()

def create_user_socials(db: Session, telegramID: str):
    """Create a new user's social media data with default values."""
    db_socials = models.UserSocials(telegramID=telegramID)
    db.add(db_socials)
    db.commit()
    db.refresh(db_socials)
    return db_socials

def update_user_socials(db: Session, telegramID: str, platform: str, username: str, verified: bool):
    """Update a user's social media data for a specific platform."""
    db_socials = db.query(models.UserSocials).filter(models.UserSocials.telegramID == telegramID).first()
    if db_socials:
        if platform == "youtube":
            db_socials.youtubeUsername = username
            db_socials.youtubeVerified = verified
        elif platform == "X":
            db_socials.XUsername = username
            db_socials.XVerified = verified
        elif platform == "instagram":
            db_socials.instaUsername = username
            db_socials.instaVerified = verified
        elif platform == "tiktok":
            db_socials.tiktokUsername = username
            db_socials.tiktokVerified = verified
        elif platform == "reddit":
            db_socials.redditUsername = username
            db_socials.redditVerified = verified
        db.commit()
        db.refresh(db_socials)
    return db_socials

# ===================== UserColony CRUD Operations =====================
def get_user_colony_members(db: Session, telegramID: str):
    """Get all members of a user's colony."""
    return db.query(models.UserColonyMembers).filter(models.UserColonyMembers.telegramID == telegramID).all()

def add_user_colony_member(db: Session, telegramID: str, memberName: str):
    """Add a new member to a user's colony."""
    db_member = models.UserColonyMembers(telegramID=telegramID, memberName=memberName)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_user_colony_elder(db: Session, telegramID: str):
    """Get a user's colony elder."""
    return db.query(models.UserColonyElder).filter(models.UserColonyElder.telegramID == telegramID).first()

def set_user_colony_elder(db: Session, telegramID: str, elderName: str):
    """Set or update a user's colony elder."""
    db_elder = db.query(models.UserColonyElder).filter(models.UserColonyElder.telegramID == telegramID).first()
    if db_elder:
        db_elder.elderName = elderName
    else:
        db_elder = models.UserColonyElder(telegramID=telegramID, elderName=elderName)
        db.add(db_elder)
    db.commit()
    db.refresh(db_elder)
    return db_elder

# ===================== Quest CRUD Operations =====================
def get_quest(db: Session, questID: int):
    """Get a quest by its ID."""
    return db.query(models.Quest).filter(models.Quest.id == questID).first()

def get_all_quests(db: Session):
    """Get all quests from the global stash."""
    return db.query(models.Quest).all()

def create_user_quest(db: Session, telegramID: str, questID: int):
    """Create a new user-specific quest."""
    db_user_quest = models.UserQuests(telegramID=telegramID, questID=questID)
    db.add(db_user_quest)
    db.commit()
    db.refresh(db_user_quest)
    return db_user_quest

def update_user_quest_progress(db: Session, telegramID: str, questID: int, currentProgress: float):
    """Update a user's quest progress."""
    db_user_quest = db.query(models.UserQuests).filter(
        models.UserQuests.telegramID == telegramID,
        models.UserQuests.questID == questID
    ).first()
    if db_user_quest:
        db_user_quest.currentProgress = currentProgress
        if db_user_quest.currentProgress >= db_user_quest.quest.requiredProgress:
            db_user_quest.completed = True
        db.commit()
        db.refresh(db_user_quest)
    return db_user_quest

def mark_user_quest_collected(db: Session, telegramID: str, questID: int):
    """Mark a user's quest as collected."""
    db_user_quest = db.query(models.UserQuests).filter(
        models.UserQuests.telegramID == telegramID,
        models.UserQuests.questID == questID
    ).first()
    if db_user_quest:
        db_user_quest.collected = True
        db.commit()
        db.refresh(db_user_quest)
    return db_user_quest

# ===================== Miner CRUD Operations =====================
def get_miner(db: Session, minerID: int):
    """Get a miner by its ID."""
    return db.query(models.Miner).filter(models.Miner.id == minerID).first()

def get_all_miners(db: Session):
    """Get all miners from the global stash."""
    return db.query(models.Miner).all()

def create_user_miner(db: Session, telegramID: str, minerID: int):
    """Create a new user-specific miner."""
    db_user_miner = models.UserMiners(telegramID=telegramID, minerID=minerID)
    db.add(db_user_miner)
    db.commit()
    db.refresh(db_user_miner)
    return db_user_miner

def update_user_miner_progress(db: Session, telegramID: str, minerID: int, currentProgress: float):
    """Update a user's miner progress."""
    db_user_miner = db.query(models.UserMiners).filter(
        models.UserMiners.telegramID == telegramID,
        models.UserMiners.minerID == minerID
    ).first()
    if db_user_miner:
        db_user_miner.currentProgress = currentProgress
        db.commit()
        db.refresh(db_user_miner)
    return db_user_miner

# ===================== Cavern CRUD Operations =====================
def get_cavern(db: Session, cavernID: int):
    """Get a cavern by its ID."""
    return db.query(models.Cavern).filter(models.Cavern.id == cavernID).first()

def get_all_caverns(db: Session):
    """Get all caverns from the global stash."""
    return db.query(models.Cavern).all()

def create_user_cavern(db: Session, telegramID: str, cavernID: int):
    """Create a new user-specific cavern."""
    db_user_cavern = models.UserCaverns(telegramID=telegramID, cavernID=cavernID)
    db.add(db_user_cavern)
    db.commit()
    db.refresh(db_user_cavern)
    return db_user_cavern

def update_user_cavern_progress(db: Session, telegramID: str, cavernID: int, currentProgress: float):
    """Update a user's cavern progress."""
    db_user_cavern = db.query(models.UserCaverns).filter(
        models.UserCaverns.telegramID == telegramID,
        models.UserCaverns.cavernID == cavernID
    ).first()
    if db_user_cavern:
        db_user_cavern.currentProgress = currentProgress
        db.commit()
        db.refresh(db_user_cavern)
    return db_user_cavern

# ===================== StoryPage CRUD Operations =====================
def get_story_page(db: Session, pageNumber: int):
    """Get a story page by its page number."""
    return db.query(models.StoryPage).filter(models.StoryPage.pageNumber == pageNumber).first()

def get_all_story_pages(db: Session):
    """Get all story pages."""
    return db.query(models.StoryPage).all()

def get_unlocked_story_pages(db: Session, highestTotalGems: float):
    """Get all story pages unlocked based on the user's highest total gems."""
    return db.query(models.StoryPage).filter(models.StoryPage.requiredGems <= highestTotalGems).all()