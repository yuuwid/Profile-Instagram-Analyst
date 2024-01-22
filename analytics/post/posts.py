import instaloader
from datetime import datetime, timedelta

from ..utils import format_date

import re


class PostScrap:
    def __init__(
        self,
        profile: instaloader.Profile,
        range_days: int = 90,
        start_date: str = None,
        end_date: str = None,
    ):
        self._profile = profile

        if end_date is not None:
            self._end_date = format_date(end_date)
        else:
            self._end_date = datetime.now()

        if start_date is not None:
            self._start_date = format_date(start_date)
        else:
            self._start_date = self._end_date - timedelta(days=range_days)

        range_days = self._end_date - self._start_date
        range_days = int(str(range_days).split(" ")[0])
        self._range_days = range_days

        self._posts = []

        self.__scrap()

    def __scrap(self):
        end_date = self._end_date
        start_date = self._start_date

        for post in self._profile.get_posts():
            post_date = post.date
            if start_date <= post_date <= end_date:
                if post.is_video:
                    temp = {
                        "likes": post.likes,
                        "comments": post.comments,
                        "views": post.video_view_count,
                        "date": post.date,
                    }
                else:
                    temp = {
                        "likes": post.likes,
                        "comments": post.comments,
                        "views": 0,
                        "date": post.date,
                    }
                self._posts.append(temp)
            else:
                if post_date < start_date:
                    break

    def scrap_caption_post(self):
        end_date = self._end_date
        start_date = self._start_date

        contents = []

        for post in self._profile.get_posts():
            post_date = post.date
            if start_date <= post_date <= end_date:
                caption = post.caption
                contents.append(caption)

        return contents

    def prepare_to_senti(self):
        end_date = self._end_date
        start_date = self._start_date

        posts_for_senti = []

        for post in self._profile.get_posts():
            post_date = post.date
            if start_date <= post_date <= end_date:
                post_url = "https://www.instagram.com/p/" + post.shortcode

                print("Scrapping:", post_url, "[START]")

                # Start Scrapping [UNDER DEVELOP]
                comments = []

                print("Scrapping:", post_url, "[DONE]")

                temp = {
                    "post_url": post_url,
                    "comments": comments,
                    "senti": {
                        "positive": 0,
                        "neutral": 0,
                        "negative": 0,
                    },
                }

                posts_for_senti.append(temp)
            else:
                if post_date < start_date:
                    break

        return posts_for_senti
