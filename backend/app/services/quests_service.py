from ..database import crud, database
from ..schemas import quests

def create_user_quest(telegramID: str, questID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_quest(db, telegramID=telegramID, questID=questID)

def update_user_quest_progress(telegramID: str, questID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_quest_progress(db, telegramID=telegramID, questID=questID, currentProgress=currentProgress)

def mark_user_quest_collected(telegramID: str, questID: int, db: Session = Depends(database.get_db)):
    return crud.mark_user_quest_collected(db, telegramID=telegramID, questID=questID)