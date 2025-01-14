from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from enum import Enum

# Enums
class VerificationStatus(str, Enum):
    no = "no"
    pending = "pending"
    yes = "yes"

class QuestType(str, Enum):
    daily = "daily"
    special = "special"

class QuestStatus(str, Enum):
    incomplete = "incomplete"
    complete = "complete"
    collected = "collected"

# User Schema
class UserBase(BaseModel):
    telegram_id: str
    username: str
    referral_code: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    last_online: datetime
    current_user_time: datetime
    overall_time_played: float
    banned: bool

    model_config = ConfigDict(from_attributes=True)

# Funds Schema
class UserFundsBase(BaseModel):
    telegram_id: str

class UserFundsCreate(UserFundsBase):
    pass

class UserFunds(UserFundsBase):
    id: int
    total_gem_count: float
    highest_gem_count: float
    overall_gem_count: float
    total_ntc_count: float
    highest_ntc_count: float
    overall_ntc_count: float

    model_config = ConfigDict(from_attributes=True)

# Tap Mining Schema
class UserTapMiningBase(BaseModel):
    telegram_id: str

class UserTapMiningCreate(UserTapMiningBase):
    pass

class UserTapMining(UserTapMiningBase):
    id: int
    daily_gems_amount: float
    mining_level: int

    model_config = ConfigDict(from_attributes=True)

# Socials Schema
class UserSocialsBase(BaseModel):
    telegram_id: str

class UserSocialsCreate(UserSocialsBase):
    pass

class UserSocials(UserSocialsBase):
    id: int
    x_username: Optional[str]
    x_follow_verified: VerificationStatus
    yt_username: Optional[str]
    yt_follow_verified: VerificationStatus
    tiktok_username: Optional[str]
    tiktok_follow_verified: VerificationStatus
    instagram_username: Optional[str]
    instagram_follow_verified: VerificationStatus
    telegram_follow_verified: VerificationStatus

    model_config = ConfigDict(from_attributes=True)

# Quests Schema
class QuestBase(BaseModel):
    quest_code: str
    type: QuestType
    icon: str
    description: str
    link: Optional[str]
    reward_amount: float
    due_date: Optional[datetime]

class QuestCreate(QuestBase):
    pass

class Quest(QuestBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class UserQuestBase(BaseModel):
    telegram_id: str
    quest_id: int

class UserQuestCreate(UserQuestBase):
    pass

class UserQuest(UserQuestBase):
    id: int
    status: QuestStatus

    model_config = ConfigDict(from_attributes=True)

# Elder Schema
class UserElderBase(BaseModel):
    telegram_id: str
    elder_telegram_id: str
    elder_username: str

class UserElderCreate(UserElderBase):
    pass

class UserElder(UserElderBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# Members Schema
class UserMembersBase(BaseModel):
    telegram_id: str
    member_telegram_id: str
    member_username: str

class UserMembersCreate(UserMembersBase):
    pass

class UserMembers(UserMembersBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# Cavern Schema
class CavernBase(BaseModel):
    name: str
    cost: float
    required_nocturnal_level: str

class CavernCreate(CavernBase):
    pass

class Cavern(CavernBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class UserCavernBase(BaseModel):
    telegram_id: str
    cavern_id: int

class UserCavernCreate(UserCavernBase):
    pass

class UserCavern(UserCavernBase):
    id: int
    purchased: bool

    model_config = ConfigDict(from_attributes=True)

# Miner Schema
class MinerBase(BaseModel):
    name: str
    cost: float
    gems_per_hour: float
    cavern_id: int

class MinerCreate(MinerBase):
    pass

class Miner(MinerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class UserMinerBase(BaseModel):
    telegram_id: str
    miner_id: int

class UserMinerCreate(UserMinerBase):
    pass

class UserMiner(UserMinerBase):
    id: int
    level: int

    model_config = ConfigDict(from_attributes=True)