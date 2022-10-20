import httpx
from fastapi import HTTPException

from core.Settings import Settings

settings = Settings()


async def get_search_query_async(query_params: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=settings.SEARCH_URL[0],
            params=query_params,
        )

        if not response:
            raise HTTPException(
                status_code=404,
                detail="Something went wrong with fetching from GNEWS"
            )

        return response.json()
