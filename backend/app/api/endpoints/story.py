from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, database
from ..schemas import story

router = APIRouter()

@router.get("/story/unlocked/", response_model=list[story.StoryPage])
def get_unlocked_story_pages(telegramID: str, db: Session = Depends(database.get_db)):
    user_gems = crud.get_user_gems(db, telegramID=telegramID)
    if not user_gems:
        raise HTTPException(status_code=404, detail="User gems not found")
    return crud.get_unlocked_story_pages(db, highestTotalGems=user_gems.highestTotalGems)