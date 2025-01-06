from pydantic import BaseModel

class UserGemsBase(BaseModel):
    telegramID: str
    totalGemCount: float
    availableGemsToMine: float
    dailyGemsMined: float

class UserGemsCreate(UserGemsBase):
    pass

class UserGems(UserGemsBase):
    id: int

    class Config:
        from_attributes = True