from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int

    class Config:
        from_attributes = True