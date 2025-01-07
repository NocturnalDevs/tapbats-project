from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, database
from ..schemas import caverns

router = APIRouter()

@router.post("/caverns/", response_model=caverns.UserCavern)
def create_user_cavern(telegramID: str, cavernID: int, db: Session = Depends(database.get_db)):
    return crud.create_user_cavern(db, telegramID=telegramID, cavernID=cavernID)

@router.put("/caverns/progress/", response_model=caverns.UserCavern)
def update_user_cavern_progress(telegramID: str, cavernID: int, currentProgress: float, db: Session = Depends(database.get_db)):
    return crud.update_user_cavern_progress(db, telegramID=telegramID, cavernID=cavernID, currentProgress=currentProgress)