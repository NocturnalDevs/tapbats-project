from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, database
from ..schemas import miners

router = APIRouter()

@router.post("/miners/", response_model=miners.UserMiner)
def create_user_miner(telegramID: str, minerID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_miner(db, telegramID=telegramID, minerID=minerID)

@router.put("/miners/progress/", response_model=miners.UserMiner)
def update_user_miner_progress(telegramID: str, minerID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_miner_progress(db, telegramID=telegramID, minerID=minerID, currentProgress=currentProgress)