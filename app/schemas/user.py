from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    login: str = Field(..., min_length=1, max_length=255)
    name: str | None = Field(default=None, max_length=255)
    email: str | None = Field(default=None, max_length=320)
    avatar_url: str | None = None
    html_url: str | None = None


class UserCreate(UserBase):
    github_id: int = Field(..., gt=0)


class UserUpdate(BaseModel):
    login: str | None = Field(default=None, min_length=1, max_length=255)
    name: str | None = Field(default=None, max_length=255)
    email: str | None = Field(default=None, max_length=320)
    avatar_url: str | None = None
    html_url: str | None = None


class UserResponse(UserBase):
    id: int
    github_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)