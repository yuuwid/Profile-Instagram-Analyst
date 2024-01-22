import instaloader
from datetime import datetime, timedelta

from .posts import PostScrap


class AvgEngagement:
    def __init__(self, profile: instaloader.Profile, scrap: PostScrap):
        self._profile = profile
        self._post_scrap = scrap

    def _get_30day_post(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        posts = []

        for post in self._post_scrap._posts:
            post_date = post["date"]
            if start_date <= post_date <= end_date:
                posts.append(post)

        return posts

    def avg_engagement_per_post(self):
        """
        Engg = SUM (Total Like + Total Comment)

        Avg. Engagement Per Post = Engg / Total Post
        """
        eng_per_post = 0

        for post in self._get_30day_post():
            n_like = post["likes"]
            n_comment = post["comments"]

            engg = n_like + n_comment
            eng_per_post += engg

        return eng_per_post / len(self._post_scrap._posts)

    def avg_likes_per_post(self):
        """
        Likes = SUM (Total Like)

        Avg. Like Per Post = Likes / Total Post
        """
        avg_like = 0

        for post in self._get_30day_post():
            n_like = post["likes"]
            rate = n_like
            avg_like += rate

        return avg_like / len(self._post_scrap._posts)

    def avg_comments_per_post(self):
        """
        Comments = SUM (Total Comment)

        Avg. Comment Per Post = Comments / Total Post
        """
        avg_comment = 0

        for post in self._post_scrap._posts:
            n_comment = post["comments"]
            rate = n_comment
            avg_comment += rate

        return avg_comment / len(self._post_scrap._posts)

    def engg_per_day(self):
        likes_comments_by_date = {}

        for post in self._get_30day_post():
            post_date = post["date"]
            formatted_date = post_date.strftime("%Y-%m-%d")
            if formatted_date not in likes_comments_by_date:
                likes_comments_by_date[formatted_date] = {
                    "likes": 0,
                    "comments": 0,
                }
            likes_comments_by_date[formatted_date]["likes"] += post["likes"]
            likes_comments_by_date[formatted_date]["comments"] += post["comments"]

        return likes_comments_by_date
