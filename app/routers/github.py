from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.github_service import get_authenticated_user
from app.services.github_sync_service import sync_github_user


router = APIRouter(
    prefix="/api/github",
    tags=["GitHub"],
)


@router.get("/me")
async def get_github_user():
    try:
        return await get_authenticated_user()

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="No fue posible consultar la API de GitHub.",
        ) from exc


@router.post("/sync")
async def synchronize_github_user(
    db: Session = Depends(get_db),
):
    try:
        github_data = await get_authenticated_user()

        user = sync_github_user(
            db=db,
            github_data=github_data,
        )

        return {
            "message": "Usuario de GitHub sincronizado correctamente.",
            "user": user,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="No fue posible sincronizar el usuario de GitHub.",
        ) from exc