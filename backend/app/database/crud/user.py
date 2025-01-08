from sqlalchemy.orm import Session
from app.models.user import User
from app.schemes.user import UserCreate

def get_user(db: Session, telegram_id: str):
    return db.query(User).filter(User.telegramID == telegram_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_last_online(db: Session, telegram_id: str, last_online):
    user = get_user(db, telegram_id)
    if user:
        user.lastOnline = last_online
        db.commit()
        db.refresh(user)
    return user