import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    API_KEY = os.getenv("API_KEY")

    TITLE = "NewSer"
    SEARCH_URL = "https://gnews.io/api/v4/search",
    TOP_URL = 'https://gnews.io/api/v4/top-headlines',

    CURRENT_COUNTRY = "us"
    DEFAULT_PARAMS = {
        "token": API_KEY,
        "country": CURRENT_COUNTRY,
    }
