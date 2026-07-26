from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.github_user import GitHubUser
from app.schemas.user import UserCreate, UserUpdate
from datetime import datetime, timezone

import logging
logger = logging.getLogger(__name__)


def get_users(
    db: Session,
    login: str | None = None,
    name: str | None = None,
    email: str | None = None,
    skip: int = 0,
    limit: int = 10,
):
    query = select(GitHubUser)

    if login:
        query = query.where(GitHubUser.login.ilike(f"%{login}%"))

    if name:
        query = query.where(GitHubUser.name.ilike(f"%{name}%"))

    if email:
        query = query.where(GitHubUser.email.ilike(f"%{email}%"))

    query = query.offset(skip).limit(limit)

    return db.scalars(query).all()


def get_user_by_id(db: Session, user_id: int):
    return db.get(GitHubUser, user_id)


def get_user_by_github_id(db: Session, github_id: int):
    query = select(GitHubUser).where(GitHubUser.github_id == github_id)
    return db.scalar(query)


def create_user(db: Session, user_data: UserCreate):
    user = GitHubUser(**user_data.model_dump())
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
    except Exception:
        db.rollback()
        logger.exception("Error al crear usuario en PostgreSQL")
        raise

    return user


def update_user(db: Session, user: GitHubUser, user_data: UserUpdate):
    update_data = user_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: GitHubUser):
    db.delete(user)
    db.commit()