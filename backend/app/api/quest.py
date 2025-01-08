from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.quest import QuestCreate, UserQuestsCreate
from app.database.crud.quest import (
    get_quest, create_quest,
    get_user_quests, create_user_quest, update_user_quest_progress
)

router = APIRouter()

# Quest Endpoints
@router.post("/quests/")
def create_quest_endpoint(quest: QuestCreate, db: Session = Depends(get_db)):
    return create_quest(db, quest)

@router.get("/quests/{quest_id}")
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = get_quest(db, quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest

# UserQuests Endpoints
@router.post("/user_quests/")
def create_user_quest_endpoint(user_quest: UserQuestsCreate, db: Session = Depends(get_db)):
    return create_user_quest(db, user_quest)

@router.get("/user_quests/{telegram_id}")
def read_user_quests(telegram_id: str, db: Session = Depends(get_db)):
    quests = get_user_quests(db, telegram_id)
    if not quests:
        raise HTTPException(status_code=404, detail="No quests found")
    return quests

@router.put("/user_quests/{user_quest_id}/progress")
def update_quest_progress(user_quest_id: int, progress: float, db: Session = Depends(get_db)):
    user_quest = update_user_quest_progress(db, user_quest_id, progress)
    if not user_quest:
        raise HTTPException(status_code=404, detail="User quest not found")
    return user_quest