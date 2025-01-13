from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, models, schemas
from ..database.connection import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user-exists/{user_id}", response_model=bool)
def check_user_exists(user_id: int, db: Session = Depends(get_db)):
    return crud.user_exists(db, user_id)

@router.get("/validate-referral-code/{referral_code}", response_model=bool)
def validate_referral_code(referral_code: str, db: Session = Depends(get_db)):
    return crud.validate_referral_code(db, referral_code)

@router.post("/save-user/", response_model=schemas.User)
def save_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user)