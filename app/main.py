import time

import requests
from cachetools import TTLCache, cached
from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from requests import Request

from api.schemas import Articles
from core.QueryManager import get_search_query_async
from core.Settings import Settings

settings = Settings()

app = FastAPI(
    title=settings.TITLE, openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
async def root():
    return RedirectResponse("https//127.0.0.1/docs")


@cached(cache=TTLCache(maxsize=128, ttl=120))
@api_router.get("/top", status_code=200, response_model=Articles)
async def top_articles(*, count: int = 10):
    params = settings.DEFAULT_PARAMS
    params['max'] = count
    params['in'] = "title, description, content"
    data = requests.get(settings.TOP_URL[0], params=params)
    return data.json()


@cached(cache=TTLCache(maxsize=128, ttl=120))
@api_router.get("/search/{keyword}", status_code=200)
async def article_search_async(*, keyword: str, count: int = 10) -> dict:
    params = settings.DEFAULT_PARAMS
    params['q'] = keyword
    params['in'] = "title, description, content"
    params['max'] = count
    data = await get_search_query_async(query_params=params)
    return data


@cached(cache=TTLCache(maxsize=128, ttl=120))
@api_router.get("/title/{keyword}", status_code=200)
async def title_search(*, keyword: str, count: int = 10):
    params = settings.DEFAULT_PARAMS
    params['q'] = keyword
    params['in'] = "title"
    params['max'] = count
    data = await get_search_query_async(query_params=params)
    return data


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001, log_level="debug")
