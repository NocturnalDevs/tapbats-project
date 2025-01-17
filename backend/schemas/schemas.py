# schemas/schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
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
class SaveUserResponse(BaseModel):
    tables: dict
    error: str = None

# Funds Schema
class UserFundsBase(BaseModel):
    telegram_id: str

class UserBase(BaseModel):
    telegram_id: str
    username: str

class UserCreate(UserBase):
    elder_referral_code: str

class UserCreateWrapper(BaseModel):
    user_data: UserCreate

class User(UserBase):
    id: int
    last_online: datetime
    current_user_time: datetime
    overall_time_played: float
    daily_gems_refreshed: bool
    banned: bool
    tap_streak: int = 0
    last_streak_update: datetime

    funds: Optional["UserFunds"] = None
    socials: Optional["UserSocials"] = None
    quests: Optional[List["UserQuest"]] = None
    members: Optional[List["UserMembers"]] = None
    elder: Optional["UserElder"] = None
    caverns: Optional[List["UserCavern"]] = None
    miners: Optional[List["UserMiner"]] = None
    tap_mining: Optional["UserTapMining"] = None
    achievements: Optional[List["UserAchievements"]] = None
    notifications: Optional[List["UserNotifications"]] = None

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
    daily_gems_amount: float

    model_config = ConfigDict(from_attributes=True)

# Socials Schema
class UserSocialsBase(BaseModel):
    telegram_id: str

class UserSocialsCreate(UserSocialsBase):
    pass

class UserSocials(UserSocialsBase):
    id: int
    x_username: Optional[str] = None
    x_follow_verified: VerificationStatus = VerificationStatus.no
    yt_username: Optional[str] = None
    yt_follow_verified: VerificationStatus = VerificationStatus.no
    tiktok_username: Optional[str] = None
    tiktok_follow_verified: VerificationStatus = VerificationStatus.no
    instagram_username: Optional[str] = None
    instagram_follow_verified: VerificationStatus = VerificationStatus.no
    telegram_follow_verified: VerificationStatus = VerificationStatus.no

    model_config = ConfigDict(from_attributes=True)

# Quests Schema
class QuestBase(BaseModel):
    type: QuestType
    icon: str
    description: str
    link: Optional[str] = None
    reward_amount: float
    due_date: Optional[datetime] = None
    repeatable: bool = False

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
    status: QuestStatus = QuestStatus.incomplete
    completion_time: Optional[datetime] = None

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
    elder_since: datetime

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
    member_since: datetime

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
    purchased: bool = False

    model_config = ConfigDict(from_attributes=True)

# Miner Schema
class MinerBase(BaseModel):
    name: str
    cost: float
    gems_per_hour: float
    cavern_id: int
    max_level: int = 10

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
    level: int = 1
    last_collection_time: datetime

    model_config = ConfigDict(from_attributes=True)

# Tap Mining Schema
class UserTapMiningBase(BaseModel):
    telegram_id: str

class UserTapMiningCreate(UserTapMiningBase):
    pass

class UserTapMining(UserTapMiningBase):
    id: int
    available_gems_to_mine: float = 0.0
    last_tap_time: datetime

    model_config = ConfigDict(from_attributes=True)

# Achievements Schema
class UserAchievementsBase(BaseModel):
    telegram_id: str
    achievement_id: int
    achievement_name: str

class UserAchievementsCreate(UserAchievementsBase):
    pass

class UserAchievements(UserAchievementsBase):
    id: int
    achieved_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Notifications Schema
class UserNotificationsBase(BaseModel):
    telegram_id: str
    message: str

class UserNotificationsCreate(UserNotificationsBase):
    pass

class UserNotifications(UserNotificationsBase):
    id: int
    created_at: datetime
    read: bool = False

    model_config = ConfigDict(from_attributes=True)