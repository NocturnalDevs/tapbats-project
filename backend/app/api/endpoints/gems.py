from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, database
from ..schemas import gems

router = APIRouter()

@router.post("/gems/", response_model=gems.UserGems)
def create_user_gems(telegramID: str, db: Session = Depends(database.get_db)):
    db_gems = crud.get_user_gems(db, telegramID=telegramID)
    if db_gems:
        raise HTTPException(status_code=400, detail="User gems already exist")
    return crud.create_user_gems(db, telegramID=telegramID)

@router.put("/gems/", response_model=gems.UserGems)
def update_user_gems(telegramID: str, totalGemCount: float, availableGemsToMine: float, dailyGemsMined: float, db: Session = Depends(database.get_db)):
    return crud.update_user_gems(db, telegramID=telegramID, totalGemCount=totalGemCount, availableGemsToMine=availableGemsToMine, dailyGemsMined=dailyGemsMined)