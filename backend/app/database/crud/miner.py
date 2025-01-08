from sqlalchemy.orm import Session
from app.models.miner import Miner, UserMiners
from app.schemes.miner import MinerCreate, UserMinersCreate

# Miner CRUD
def get_miner(db: Session, miner_id: int):
    return db.query(Miner).filter(Miner.id == miner_id).first()

def create_miner(db: Session, miner: MinerCreate):
    db_miner = Miner(**miner.dict())
    db.add(db_miner)
    db.commit()
    db.refresh(db_miner)
    return db_miner

# UserMiners CRUD
def get_user_miners(db: Session, telegram_id: str):
    return db.query(UserMiners).filter(UserMiners.telegramID == telegram_id).all()

def create_user_miner(db: Session, user_miner: UserMinersCreate):
    db_user_miner = UserMiners(**user_miner.dict())
    db.add(db_user_miner)
    db.commit()
    db.refresh(db_user_miner)
    return db_user_miner

def update_user_miner_progress(db: Session, user_miner_id: int, progress: float):
    user_miner = db.query(UserMiners).filter(UserMiners.id == user_miner_id).first()
    if user_miner:
        user_miner.currentProgress = progress
        if user_miner.currentProgress >= user_miner.miner.requiredProgress:
            user_miner.owned = True
        db.commit()
        db.refresh(user_miner)
    return user_miner