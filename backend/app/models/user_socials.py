from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

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