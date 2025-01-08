from sqlalchemy.orm import Session
from app.models.user_socials import UserSocials
from app.schemes.user_socials import UserSocialsCreate

def get_user_socials(db: Session, telegram_id: str):
    return db.query(UserSocials).filter(UserSocials.telegramID == telegram_id).first()

def create_user_socials(db: Session, user_socials: UserSocialsCreate):
    db_user_socials = UserSocials(**user_socials.dict())
    db.add(db_user_socials)
    db.commit()
    db.refresh(db_user_socials)
    return db_user_socials

def update_user_socials(db: Session, telegram_id: str, socials_data: dict):
    user_socials = get_user_socials(db, telegram_id)
    if user_socials:
        for key, value in socials_data.items():
            setattr(user_socials, key, value)
        db.commit()
        db.refresh(user_socials)
    return user_socials