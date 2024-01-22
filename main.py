from analytics.insta import InstaLytic

from typing import Union
from fastapi import FastAPI

app = FastAPI()
# Run API: 
# uvicorn main:app --reload


@app.post("/profile-report")
def profile_report(username: str):
    i = InstaLytic(username)
    return i.profile_report()


@app.post("/er-report")
def posts_report(
    username: str,
    range_date: int = 90,
    start_date: str = None,
    end_date: str = None,
):
    i = InstaLytic(username, range_date, start_date, end_date)
    return i.posts_report()


@app.post("/average-engagement")
def average_engagement(
    username: str,
    range_date: int = 90,
    start_date: str = None,
    end_date: str = None,
):
    i = InstaLytic(username, range_date, start_date, end_date)
    return i.average_engagement()


@app.post("/average-posts")
def average_posts(
    username: str,
    range_date: int = 90,
    start_date: str = None,
    end_date: str = None,
):
    i = InstaLytic(username, range_date, start_date, end_date)
    return i.average_posts()


@app.post("/content-report")
def content_report(
    username: str,
    range_date: int = 90,
    start_date: str = None,
    end_date: str = None,
):
    i = InstaLytic(username, range_date, start_date, end_date)
    return i.content_report()


# username = "indomie"
# i = InstaLytic(username)
# print(i.profile_report())
# print(i.posts_report())
# print(i.average_engagement())
# print(i.average_posts())
# print(i.content_report())

# i.sentiment_comments()
