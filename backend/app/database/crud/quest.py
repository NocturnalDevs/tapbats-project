from sqlalchemy.orm import Session
from app.models.quest import Quest, UserQuests
from app.schemes.quest import QuestCreate, UserQuestsCreate

# Quest CRUD
def get_quest(db: Session, quest_id: int):
    return db.query(Quest).filter(Quest.id == quest_id).first()

def create_quest(db: Session, quest: QuestCreate):
    db_quest = Quest(**quest.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

# UserQuests CRUD
def get_user_quests(db: Session, telegram_id: str):
    return db.query(UserQuests).filter(UserQuests.telegramID == telegram_id).all()

def create_user_quest(db: Session, user_quest: UserQuestsCreate):
    db_user_quest = UserQuests(**user_quest.dict())
    db.add(db_user_quest)
    db.commit()
    db.refresh(db_user_quest)
    return db_user_quest

def update_user_quest_progress(db: Session, user_quest_id: int, progress: float):
    user_quest = db.query(UserQuests).filter(UserQuests.id == user_quest_id).first()
    if user_quest:
        user_quest.currentProgress = progress
        if user_quest.currentProgress >= user_quest.quest.requiredProgress:
            user_quest.completed = True
        db.commit()
        db.refresh(user_quest)
    return user_quest