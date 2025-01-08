from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemes.user_colony import UserColonyMembersCreate, UserColonyElderCreate
from app.database.crud.user_colony import (
    get_user_colony_members, create_user_colony_member,
    get_user_colony_elder, create_user_colony_elder
)

router = APIRouter()

# UserColonyMembers Endpoints
@router.post("/user_colony_members/")
def create_colony_member(member: UserColonyMembersCreate, db: Session = Depends(get_db)):
    return create_user_colony_member(db, member)

@router.get("/user_colony_members/{telegram_id}")
def read_colony_members(telegram_id: str, db: Session = Depends(get_db)):
    members = get_user_colony_members(db, telegram_id)
    if not members:
        raise HTTPException(status_code=404, detail="No colony members found")
    return members

# UserColonyElder Endpoints
@router.post("/user_colony_elder/")
def create_colony_elder(elder: UserColonyElderCreate, db: Session = Depends(get_db)):
    return create_user_colony_elder(db, elder)

@router.get("/user_colony_elder/{telegram_id}")
def read_colony_elder(telegram_id: str, db: Session = Depends(get_db)):
    elder = get_user_colony_elder(db, telegram_id)
    if not elder:
        raise HTTPException(status_code=404, detail="Colony elder not found")
    return elder