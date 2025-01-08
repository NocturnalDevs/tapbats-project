from ..database import crud, database
from ..schemes import cavern

def create_user_cavern(telegramID: str, cavernID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_cavern(db, telegramID=telegramID, cavernID=cavernID)

def update_user_cavern_progress(telegramID: str, cavernID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_cavern_progress(db, telegramID=telegramID, cavernID=cavernID, currentProgress=currentProgress)