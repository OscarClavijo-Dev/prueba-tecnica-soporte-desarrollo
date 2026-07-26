from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.github_user import GitHubUser


def sync_github_user(
    db: Session,
    github_data: dict,
) -> GitHubUser:
    github_id = github_data["id"]

    existing_user = db.scalar(
        select(GitHubUser).where(
            GitHubUser.github_id == github_id
        )
    )

    now = datetime.now(timezone.utc)

    if existing_user is None:
        user = GitHubUser(
            github_id=github_id,
            login=github_data["login"],
            name=github_data.get("name"),
            email=github_data.get("email"),
            avatar_url=github_data.get("avatar_url"),
            html_url=github_data.get("html_url"),
            created_at=now,
            updated_at=now,
        )

        db.add(user)

    else:
        existing_user.login = github_data["login"]
        existing_user.name = github_data.get("name")
        existing_user.email = github_data.get("email")
        existing_user.avatar_url = github_data.get("avatar_url")
        existing_user.html_url = github_data.get("html_url")
        existing_user.updated_at = now

        user = existing_user

    try:
        db.commit()
        db.refresh(user)

    except Exception:
        db.rollback()
        raise

    return user