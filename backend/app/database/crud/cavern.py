from sqlalchemy.orm import Session
from app.models.cavern import Cavern, UserCaverns
from app.schemes.cavern import CavernCreate, UserCavernsCreate

# Cavern CRUD
def get_cavern(db: Session, cavern_id: int):
    return db.query(Cavern).filter(Cavern.id == cavern_id).first()

def create_cavern(db: Session, cavern: CavernCreate):
    db_cavern = Cavern(**cavern.dict())
    db.add(db_cavern)
    db.commit()
    db.refresh(db_cavern)
    return db_cavern

# UserCaverns CRUD
def get_user_caverns(db: Session, telegram_id: str):
    return db.query(UserCaverns).filter(UserCaverns.telegramID == telegram_id).all()

def create_user_cavern(db: Session, user_cavern: UserCavernsCreate):
    db_user_cavern = UserCaverns(**user_cavern.dict())
    db.add(db_user_cavern)
    db.commit()
    db.refresh(db_user_cavern)
    return db_user_cavern

def update_user_cavern_progress(db: Session, user_cavern_id: int, progress: float):
    user_cavern = db.query(UserCaverns).filter(UserCaverns.id == user_cavern_id).first()
    if user_cavern:
        user_cavern.currentProgress = progress
        if user_cavern.currentProgress >= user_cavern.cavern.requiredProgress:
            user_cavern.owned = True
        db.commit()
        db.refresh(user_cavern)
    return user_cavern