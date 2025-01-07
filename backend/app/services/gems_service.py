from ..database import crud, database
from ..schemas import gems

def get_user_gems(telegramID: str, db: Session = Depends(database.get_db)):
    return crud.get_user_gems(db, telegramID=telegramID)

def update_user_gems(telegramID: str, totalGemCount: float, availableGemsToMine: float, dailyGemsMined: float, db: Session = Depends(database.get_db)):
    return crud.update_user_gems(db, telegramID=telegramID, totalGemCount=totalGemCount, availableGemsToMine=availableGemsToMine, dailyGemsMined=dailyGemsMined)