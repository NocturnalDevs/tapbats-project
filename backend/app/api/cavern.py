from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.cavern import CavernCreate, UserCavernsCreate
from app.database.crud.cavern import (
    get_cavern, create_cavern,
    get_user_caverns, create_user_cavern, update_user_cavern_progress
)

router = APIRouter()

# Cavern Endpoints
@router.post("/caverns/")
def create_cavern_endpoint(cavern: CavernCreate, db: Session = Depends(get_db)):
    return create_cavern(db, cavern)

@router.get("/caverns/{cavern_id}")
def read_cavern(cavern_id: int, db: Session = Depends(get_db)):
    cavern = get_cavern(db, cavern_id)
    if not cavern:
        raise HTTPException(status_code=404, detail="Cavern not found")
    return cavern

# UserCaverns Endpoints
@router.post("/user_caverns/")
def create_user_cavern_endpoint(user_cavern: UserCavernsCreate, db: Session = Depends(get_db)):
    return create_user_cavern(db, user_cavern)

@router.get("/user_caverns/{telegram_id}")
def read_user_caverns(telegram_id: str, db: Session = Depends(get_db)):
    caverns = get_user_caverns(db, telegram_id)
    if not caverns:
        raise HTTPException(status_code=404, detail="No caverns found")
    return caverns

@router.put("/user_caverns/{user_cavern_id}/progress")
def update_cavern_progress(user_cavern_id: int, progress: float, db: Session = Depends(get_db)):
    user_cavern = update_user_cavern_progress(db, user_cavern_id, progress)
    if not user_cavern:
        raise HTTPException(status_code=404, detail="User cavern not found")
    return user_cavern