from ..database import crud, database
from ..schemes import miner

def create_user_miner(telegramID: str, minerID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_miner(db, telegramID=telegramID, minerID=minerID)

def update_user_miner_progress(telegramID: str, minerID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_miner_progress(db, telegramID=telegramID, minerID=minerID, currentProgress=currentProgress)