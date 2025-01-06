from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import crud, database  # Updated import
from app.schemas import gems  # Updated import

router = APIRouter()

@router.get("/gems/{telegramID}", response_model=gems.UserGems)
def read_gems(telegramID: str, db: Session = Depends(database.get_db)):
    db_gems = crud.get_user_gems(db, telegramID=telegramID)
    if db_gems is None:
        raise HTTPException(status_code=404, detail="Gems not found")
    return db_gems

@router.post("/gems/{telegramID}", response_model=gems.UserGems)
def update_gems(telegramID: str, gems_update: gems.UserGemsBase, db: Session = Depends(database.get_db)):
    db_gems = crud.update_user_gems(
        db,
        telegramID=telegramID,
        totalGemCount=gems_update.totalGemCount,
        availableGemsToMine=gems_update.availableGemsToMine,
        dailyGemsMined=gems_update.dailyGemsMined
    )
    if db_gems is None:
        raise HTTPException(status_code=404, detail="Gems not found")
    return db_gems