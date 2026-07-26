from fastapi import APIRouter, HTTPException

from app.services.github_service import get_authenticated_user


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