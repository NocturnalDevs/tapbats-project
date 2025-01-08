from sqlalchemy.orm import Session
from app.models.user_gems import UserGems
from app.schemes.user_gems import UserGemsCreate

def get_user_gems(db: Session, telegram_id: str):
    return db.query(UserGems).filter(UserGems.telegramID == telegram_id).first()

def create_user_gems(db: Session, user_gems: UserGemsCreate):
    db_user_gems = UserGems(**user_gems.dict())
    db.add(db_user_gems)
    db.commit()
    db.refresh(db_user_gems)
    return db_user_gems

def update_user_gems(db: Session, telegram_id: str, gem_count: float):
    user_gems = get_user_gems(db, telegram_id)
    if user_gems:
        user_gems.totalGemCount += gem_count
        if user_gems.totalGemCount > user_gems.highestTotalGems:
            user_gems.highestTotalGems = user_gems.totalGemCount
        db.commit()
        db.refresh(user_gems)
    return user_gems