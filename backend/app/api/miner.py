from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.miner import MinerCreate, UserMinersCreate
from app.database.crud.miner import (
    get_miner, create_miner,
    get_user_miners, create_user_miner, update_user_miner_progress
)

router = APIRouter()

# Miner Endpoints
@router.post("/miners/")
def create_miner_endpoint(miner: MinerCreate, db: Session = Depends(get_db)):
    return create_miner(db, miner)

@router.get("/miners/{miner_id}")
def read_miner(miner_id: int, db: Session = Depends(get_db)):
    miner = get_miner(db, miner_id)
    if not miner:
        raise HTTPException(status_code=404, detail="Miner not found")
    return miner

# UserMiners Endpoints
@router.post("/user_miners/")
def create_user_miner_endpoint(user_miner: UserMinersCreate, db: Session = Depends(get_db)):
    return create_user_miner(db, user_miner)

@router.get("/user_miners/{telegram_id}")
def read_user_miners(telegram_id: str, db: Session = Depends(get_db)):
    miners = get_user_miners(db, telegram_id)
    if not miners:
        raise HTTPException(status_code=404, detail="No miners found")
    return miners

@router.put("/user_miners/{user_miner_id}/progress")
def update_miner_progress(user_miner_id: int, progress: float, db: Session = Depends(get_db)):
    user_miner = update_user_miner_progress(db, user_miner_id, progress)
    if not user_miner:
        raise HTTPException(status_code=404, detail="User miner not found")
    return user_miner