from pydantic import BaseModel
from datetime import datetime

# Base schema for Quest
class QuestBase(BaseModel):
    type: str
    description: str
    rewardAmount: float
    link: str | None = None
    requiredProgress: float | None = None

# Schema for creating Quest
class QuestCreate(QuestBase):
    pass

# Schema for returning Quest
class Quest(QuestBase):
    id: int

    class Config:
        from_attributes = True

# Base schema for UserQuests
class UserQuestsBase(BaseModel):
    telegramID: str
    questID: int
    currentProgress: float
    completed: bool
    collected: bool
    due: datetime | None = None

# Schema for creating UserQuests
class UserQuestsCreate(UserQuestsBase):
    pass

# Schema for returning UserQuests
class UserQuests(UserQuestsBase):
    id: int

    class Config:
        from_attributes = True