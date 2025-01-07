from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, database
from ..schemas import quests

router = APIRouter()

@router.post("/quests/", response_model=quests.UserQuest)
def create_user_quest(telegramID: str, questID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_quest(db, telegramID=telegramID, questID=questID)

@router.put("/quests/progress/", response_model=quests.UserQuest)
def update_user_quest_progress(telegramID: str, questID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_quest_progress(db, telegramID=telegramID, questID=questID, currentProgress=currentProgress)

@router.put("/quests/collect/", response_model=quests.UserQuest)
def mark_user_quest_collected(telegramID: str, questID: int, db: Session = Depends(database.get_db)):
    return crud.mark_user_quest_collected(db, telegramID=telegramID, questID=questID)