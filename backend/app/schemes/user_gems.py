from pydantic import BaseModel

# Base schema for UserGems
class UserGemsBase(BaseModel):
    telegramID: str
    totalGemCount: float
    highestTotalGems: float
    availableGemsToMine: float
    dailyGemsMined: float
    mineTapLevel: int
    gemRechargeLevel: int

# Schema for creating UserGems
class UserGemsCreate(UserGemsBase):
    pass

# Schema for returning UserGems
class UserGems(UserGemsBase):
    id: int

    class Config:
        from_attributes = True