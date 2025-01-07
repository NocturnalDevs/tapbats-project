from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# User Table
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, unique=True, index=True)
    lastOnline = Column(DateTime)
    referralCode = Column(String, unique=True)

    # Relationships
    gems = relationship("UserGems", back_populates="user")
    socials = relationship("UserSocials", back_populates="user")
    colony_members = relationship("UserColonyMembers", back_populates="user")
    colony_elder = relationship("UserColonyElder", back_populates="user")
    quests = relationship("UserQuests", back_populates="user")
    miners = relationship("UserMiners", back_populates="user")
    caverns = relationship("UserCaverns", back_populates="user")

# UserGems Table
class UserGems(Base):
    __tablename__ = "user_gems"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    totalGemCount = Column(Float, default=0)
    highestTotalGems = Column(Float, default=0)
    availableGemsToMine = Column(Float, default=0)
    dailyGemsMined = Column(Float, default=0)
    mineTapLevel = Column(Integer, default=1)
    gemRechargeLevel = Column(Integer, default=1)
    # mineTapAmount = Column(Float, default=10)
    # gemRechargeAmountPerSec = Column(Float, default=1)

    user = relationship("User", back_populates="gems")

# UserSocials Table
class UserSocials(Base):
    __tablename__ = "user_socials"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    youtubeUsername = Column(String, nullable=True)
    youtubeVerified = Column(Boolean, default=False)
    XUsername = Column(String, nullable=True)
    XVerified = Column(Boolean, default=False)
    instaUsername = Column(String, nullable=True)
    instaVerified = Column(Boolean, default=False)
    tiktokUsername = Column(String, nullable=True)
    tiktokVerified = Column(Boolean, default=False)
    redditUsername = Column(String, nullable=True)
    redditVerified = Column(Boolean, default=False)

    user = relationship("User", back_populates="socials")

# UserColonyMembers Table
class UserColonyMembers(Base):
    __tablename__ = "user_colony_members"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    memberName = Column(String)

    user = relationship("User", back_populates="colony_members")

# UserColonyElder Table
class UserColonyElder(Base):
    __tablename__ = "user_colony_elder"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    elderName = Column(String)

    user = relationship("User", back_populates="colony_elder")

# Quest Table (Global stash of quests)
class Quest(Base):
    __tablename__ = "quest"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # 'daily' or 'special'
    description = Column(String)
    rewardAmount = Column(Float)
    link = Column(String, nullable=True)  # Optional link for social quests
    requiredProgress = Column(Float, nullable=True)  # Optional for progress-based quests

# UserQuests Table (User-specific quests)
class UserQuests(Base):
    __tablename__ = "user_quests"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    questID = Column(Integer, ForeignKey("quest.id"))
    currentProgress = Column(Float, default=0)
    completed = Column(Boolean, default=False)
    collected = Column(Boolean, default=False)
    due = Column(DateTime, nullable=True)  # Optional for daily quests

    user = relationship("User", back_populates="quests")
    quest = relationship("Quest")

# Miner Table (Global stash of miners)
class Miner(Base):
    __tablename__ = "miner"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    mineAmountPerSec = Column(Float)
    levelUpGemRequirement = Column(Float)
    requiredProgress = Column(Float)  # Progress required to unlock

# UserMiners Table (User-specific miners)
class UserMiners(Base):
    __tablename__ = "user_miners"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    minerID = Column(Integer, ForeignKey("miner.id"))
    owned = Column(Boolean, default=False)
    currentLevel = Column(Integer, default=1)
    currentProgress = Column(Float, default=0)

    user = relationship("User", back_populates="miners")
    miner = relationship("Miner")

# Cavern Table (Global stash of caverns)
class Cavern(Base):
    __tablename__ = "cavern"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    requiredProgress = Column(Float)  # Progress required to unlock

# UserCaverns Table (User-specific caverns)
class UserCaverns(Base):
    __tablename__ = "user_caverns"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    cavernID = Column(Integer, ForeignKey("cavern.id"))
    owned = Column(Boolean, default=False)
    currentProgress = Column(Float, default=0)

    user = relationship("User", back_populates="caverns")
    cavern = relationship("Cavern")

# StoryPage Table
class StoryPage(Base):
    __tablename__ = "story_page"
    id = Column(Integer, primary_key=True, index=True)
    pageNumber = Column(Integer)
    URL = Column(String)  # Path to the image
    requiredGems = Column(Float)  # Gems required to unlock