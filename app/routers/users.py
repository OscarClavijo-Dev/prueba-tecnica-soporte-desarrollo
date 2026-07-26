from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services import user_service


router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[UserResponse],
    summary="Consultar usuarios",
    description="Obtiene los usuarios almacenados en PostgreSQL con filtros opcionales.",
)
def list_users(
    login: str | None = Query(default=None),
    name: str | None = Query(default=None),
    email: str | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return user_service.get_users(
        db=db,
        login=login,
        name=name,
        email=email,
        skip=skip,
        limit=limit,
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Consultar usuario por identificador",
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    return user


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario",
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = user_service.get_user_by_github_id(
        db,
        user_data.github_id,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese github_id",
        )

    try:
        return user_service.create_user(db, user_data)

    except IntegrityError as exc:
        db.rollback()
        error_text = str(getattr(exc, "orig", exc))

        if "github_users_github_id_key" in error_text:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un usuario con ese github_id",
            )

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No fue posible crear el usuario debido a una restricción de integridad",
        )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Actualizar usuario",
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    return user_service.update_user(
        db,
        user,
        user_data,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar usuario",
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    user_service.delete_user(db, user)