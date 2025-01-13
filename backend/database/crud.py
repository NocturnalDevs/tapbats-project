from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_exists(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first() is not None

def validate_referral_code(db: Session, referral_code: str):
    return db.query(models.User).filter(models.User.referral_code == referral_code).first() is not None