from pydantic import BaseModel
from datetime import datetime

class QuestBase(BaseModel):
    type: str
    description: str
    rewardAmount: float
    link: str | None = None
    requiredProgress: float | None = None

class QuestCreate(QuestBase):
    pass

class Quest(QuestBase):
    id: int

    class Config:
        from_attributes = True

class UserQuestBase(BaseModel):
    telegramID: str
    questID: int

class UserQuestCreate(UserQuestBase):
    pass

class UserQuest(UserQuestBase):
    id: int
    currentProgress: float
    completed: bool
    collected: bool
    due: datetime | None = None

    class Config:
        from_attributes = True