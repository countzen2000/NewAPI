from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    url: str
    image: str
    publishedAt: str
    source: dict
    description: str
    content: str


class Articles(BaseModel):
    totalArticles: int
    articles: List[Article] = []
