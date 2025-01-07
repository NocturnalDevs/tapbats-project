from pydantic import BaseModel

class StoryPageBase(BaseModel):
    pageNumber: int
    URL: str
    requiredGems: float

class StoryPageCreate(StoryPageBase):
    pass

class StoryPage(StoryPageBase):
    id: int

    class Config:
        from_attributes = True