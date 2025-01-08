from pydantic import BaseModel

# Base schema for UserSocials
class UserSocialsBase(BaseModel):
    telegramID: str
    youtubeUsername: str | None = None
    youtubeVerified: bool
    XUsername: str | None = None
    XVerified: bool
    instaUsername: str | None = None
    instaVerified: bool
    tiktokUsername: str | None = None
    tiktokVerified: bool
    redditUsername: str | None = None
    redditVerified: bool

# Schema for creating UserSocials
class UserSocialsCreate(UserSocialsBase):
    pass

# Schema for returning UserSocials
class UserSocials(UserSocialsBase):
    id: int

    class Config:
        from_attributes = True