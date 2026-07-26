import asyncio

from app.services.github_service import get_authenticated_user


async def main():
    user = await get_authenticated_user()

    print("Usuario autenticado:")
    print(user)


if __name__ == "__main__":
    asyncio.run(main())