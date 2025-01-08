from sqlalchemy.orm import Session
from app.models.user_colony import UserColonyMembers, UserColonyElder
from app.schemes.user_colony import UserColonyMembersCreate, UserColonyElderCreate

# UserColonyMembers CRUD
def get_user_colony_members(db: Session, telegram_id: str):
    return db.query(UserColonyMembers).filter(UserColonyMembers.telegramID == telegram_id).all()

def create_user_colony_member(db: Session, member: UserColonyMembersCreate):
    db_member = UserColonyMembers(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

# UserColonyElder CRUD
def get_user_colony_elder(db: Session, telegram_id: str):
    return db.query(UserColonyElder).filter(UserColonyElder.telegramID == telegram_id).first()

def create_user_colony_elder(db: Session, elder: UserColonyElderCreate):
    db_elder = UserColonyElder(**elder.dict())
    db.add(db_elder)
    db.commit()
    db.refresh(db_elder)
    return db_elder