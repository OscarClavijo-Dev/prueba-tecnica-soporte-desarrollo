import httpx

from app.config import settings


GITHUB_API_URL = "https://api.github.com"


async def get_authenticated_user():
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {settings.github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{GITHUB_API_URL}/user",
                headers=headers,
            )

        response.raise_for_status()

        return response.json()

    except httpx.HTTPStatusError as exc:
        raise RuntimeError(
            f"GitHub rechazó la solicitud. Código HTTP: {exc.response.status_code}"
        ) from exc

    except httpx.RequestError as exc:
        raise RuntimeError(
            "No fue posible establecer comunicación con GitHub."
        ) from exc