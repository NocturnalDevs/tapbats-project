from pydantic import BaseModel

# Base schema for UserColonyMembers
class UserColonyMembersBase(BaseModel):
    telegramID: str
    memberName: str

# Schema for creating UserColonyMembers
class UserColonyMembersCreate(UserColonyMembersBase):
    pass

# Schema for returning UserColonyMembers
class UserColonyMembers(UserColonyMembersBase):
    id: int

    class Config:
        from_attributes = True

# Base schema for UserColonyElder
class UserColonyElderBase(BaseModel):
    telegramID: str
    elderName: str

# Schema for creating UserColonyElder
class UserColonyElderCreate(UserColonyElderBase):
    pass

# Schema for returning UserColonyElder
class UserColonyElder(UserColonyElderBase):
    id: int

    class Config:
        from_attributes = True