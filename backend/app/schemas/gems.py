from pydantic import BaseModel

class UserGemsBase(BaseModel):
    telegramID: str

class UserGemsCreate(UserGemsBase):
    pass

class UserGems(UserGemsBase):
    id: int
    totalGemCount: float
    highestTotalGems: float
    availableGemsToMine: float
    dailyGemsMined: float
    mineTapLevel: int
    gemRechargeLevel: int

    class Config:
        from_attributes = True