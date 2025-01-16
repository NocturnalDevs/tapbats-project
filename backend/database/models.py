from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Define enums
VerificationStatus = Enum("no", "pending", "yes", name="verification_status")
QuestType = Enum("daily", "special", name="quest_type")
QuestStatus = Enum("incomplete", "complete", "collected", name="quest_status")

# User Table
class UserTable(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    referral_code = Column(String, unique=True, nullable=False)
    last_online = Column(DateTime, default=datetime.utcnow)
    current_user_time = Column(DateTime, default=datetime.utcnow)
    overall_time_played = Column(Float, default=0.0)
    daily_gems_refreshed = Column(Boolean, default=False)
    banned = Column(Boolean, default=False)

    # Relationships
    funds = relationship("UserFundsTable", uselist=False, back_populates="user")
    socials = relationship("UserSocialsTable", uselist=False, back_populates="user")
    quests = relationship("UserQuestTable", back_populates="user")
    elder = relationship("UserElderTable", uselist=False, back_populates="user")
    members = relationship("UserMembersTable", back_populates="user")
    caverns = relationship("UserCavernTable", back_populates="user")
    miners = relationship("UserMinerTable", back_populates="user")

# User Funds Table
class UserFundsTable(Base):
    __tablename__ = "user_funds_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    total_gem_count = Column(Float, default=0.0)
    highest_gem_count = Column(Float, default=0.0)
    overall_gem_count = Column(Float, default=0.0)
    total_ntc_count = Column(Float, default=0.0)
    highest_ntc_count = Column(Float, default=0.0)
    overall_ntc_count = Column(Float, default=0.0)
    daily_gems_amount = Column(Float, default=75.0)  # Default for Fledgling

    # Relationships
    user = relationship("UserTable", back_populates="funds")

# Cavern Table (Constant/Default Values)
class CavernTable(Base):
    __tablename__ = "cavern_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    required_nocturnal_level = Column(String, nullable=False)

# Miner Table (Constant/Default Values)
class MinerTable(Base):
    __tablename__ = "miner_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    gems_per_hour = Column(Float, nullable=False)
    cavern_id = Column(Integer, ForeignKey("cavern_table.id"), nullable=False)

    # Relationships
    cavern = relationship("CavernTable")

# User Cavern Table (Links Users to Caverns)
class UserCavernTable(Base):
    __tablename__ = "user_cavern_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    cavern_id = Column(Integer, ForeignKey("cavern_table.id"), nullable=False)
    purchased = Column(Boolean, default=False)

    # Relationships
    user = relationship("UserTable", back_populates="caverns")
    cavern = relationship("CavernTable")

# User Miner Table (Links Users to Miners)
class UserMinerTable(Base):
    __tablename__ = "user_miner_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    miner_id = Column(Integer, ForeignKey("miner_table.id"), nullable=False)
    level = Column(Integer, default=0)

    # Relationships
    user = relationship("UserTable", back_populates="miners")
    miner = relationship("MinerTable")

# User Socials Table
class UserSocialsTable(Base):
    __tablename__ = "user_socials_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    x_username = Column(String)
    x_follow_verified = Column(VerificationStatus, default="no")
    yt_username = Column(String)
    yt_follow_verified = Column(VerificationStatus, default="no")
    tiktok_username = Column(String)
    tiktok_follow_verified = Column(VerificationStatus, default="no")
    instagram_username = Column(String)
    instagram_follow_verified = Column(VerificationStatus, default="no")
    telegram_follow_verified = Column(VerificationStatus, default="no")

    # Relationships
    user = relationship("UserTable", back_populates="socials")

# Quest Table (Constant/Default Values)
class QuestTable(Base):
    __tablename__ = "quest_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(QuestType, nullable=False)
    icon = Column(String, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String)
    reward_amount = Column(Float, nullable=False)
    due_date = Column(DateTime)

# User Quest Table (Links Users to Quests)
class UserQuestTable(Base):
    __tablename__ = "user_quest_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    quest_id = Column(Integer, ForeignKey("quest_table.id"), nullable=False)
    status = Column(QuestStatus, default="incomplete")

    # Relationships
    user = relationship("UserTable", back_populates="quests")
    quest = relationship("QuestTable")

# User Elder Table
class UserElderTable(Base):
    __tablename__ = "user_elder_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    elder_telegram_id = Column(String, nullable=False)
    elder_username = Column(String, nullable=False)

    # Relationships
    user = relationship("UserTable", back_populates="elder")

# User Members Table
class UserMembersTable(Base):
    __tablename__ = "user_members_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, ForeignKey("user_table.telegram_id"), nullable=False)
    member_telegram_id = Column(String, nullable=False)
    member_username = Column(String, nullable=False)

    # Relationships
    user = relationship("UserTable", back_populates="members")