from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GitHubUserResponse(BaseModel):
    id: int
    github_id: int
    login: str
    name: str | None = None
    email: str | None = None
    avatar_url: str | None = None
    html_url: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)