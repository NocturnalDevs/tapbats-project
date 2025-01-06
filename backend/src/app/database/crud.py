from sqlalchemy.orm import Session
from . import models

# User CRUD Operations
def get_user(db: Session, telegramID: str):
    return db.query(models.User).filter(models.User.telegramID == telegramID).first()

def create_user(db: Session, telegramID: str):
    db_user = models.User(telegramID=telegramID)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# UserGems CRUD Operations
def get_user_gems(db: Session, telegramID: str):
    return db.query(models.UserGems).filter(models.UserGems.telegramID == telegramID).first()

def update_user_gems(db: Session, telegramID: str, totalGemCount: float, availableGemsToMine: float, dailyGemsMined: float):
    db_gems = db.query(models.UserGems).filter(models.UserGems.telegramID == telegramID).first()
    if db_gems:
        db_gems.totalGemCount = totalGemCount
        db_gems.availableGemsToMine = availableGemsToMine
        db_gems.dailyGemsMined = dailyGemsMined
        db.commit()
        db.refresh(db_gems)
    return db_gems

# Quest CRUD Operations
def get_quest(db: Session, questID: int):
    return db.query(models.Quest).filter(models.Quest.id == questID).first()

def create_user_quest(db: Session, telegramID: str, questID: int):
    db_user_quest = models.UserQuests(telegramID=telegramID, questID=questID)
    db.add(db_user_quest)
    db.commit()
    db.refresh(db_user_quest)
    return db_user_quest

# Add more CRUD operations as needed...