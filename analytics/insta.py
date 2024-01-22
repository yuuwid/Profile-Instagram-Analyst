import instaloader
from .post.posts import PostScrap
from .post.rate_lytics import PostRateLytic
from .post.average_engagement import AvgEngagement
from .post.avg_post import AvgPost
from .post.content import Content


class InstaLytic:
    def __init__(
        self,
        username: str,
        range_days: int = 90,
        start_date: str = None,
        end_date: str = None,
    ):
        self._username = username
        self._loader = instaloader.Instaloader()

        self._profile = instaloader.Profile.from_username(
            self._loader.context,
            username,
        )

        self._post_scrap = PostScrap(self._profile, range_days, start_date, end_date)

    def profile_report(self):
        full_name = self._profile.full_name
        username = self._profile.username
        bio = self._profile.biography

        total_post = self._profile.mediacount
        followers = self._profile.followers
        following = self._profile.followees

        profile_picture = self._profile.profile_pic_url
        is_verified = self._profile.is_verified
        is_private = self._profile.is_private

        return {
            "profile": {
                "username": username,
                "is_verified": is_verified,
                "profile_picture": profile_picture,
                "full_name": full_name,
                "bio": bio,
                "total_post": total_post,
                "followers": followers,
                "following": following,
                "is_private": is_private,
            },
            "options": {
                "username": self._username,
                "range_days": self._post_scrap._range_days,
                "start_date": self._post_scrap._start_date,
                "end_date": self._post_scrap._end_date,
            },
        }

    def posts_report(self):
        postL = PostRateLytic(profile=self._profile, scrap=self._post_scrap)
        return {
            "report": {
                "engagement_rate": postL.count_engagement_rate(),
                "like_rate": postL.count_like_rate(),
                "comment_rate": postL.count_comment_rate(),
            },
            "options": {
                "username": self._username,
                "range_days": self._post_scrap._range_days,
                "start_date": self._post_scrap._start_date,
                "end_date": self._post_scrap._end_date,
            },
        }

    def average_engagement(self):
        avgegg = AvgEngagement(profile=self._profile, scrap=self._post_scrap)

        return {
            "report": {
                "avg_engagement_rate": avgegg.avg_engagement_per_post(),
                "avg_like_rate": avgegg.avg_likes_per_post(),
                "avg_comment_rate": avgegg.avg_comments_per_post(),
                "avg_30_post": avgegg.engg_per_day(),
            },
            "options": {
                "username": self._username,
                "range_days": self._post_scrap._range_days,
                "start_date": self._post_scrap._start_date,
                "end_date": self._post_scrap._end_date,
            },
        }

    def average_posts(self):
        avgP = AvgPost(profile=self._profile, scrap=self._post_scrap)

        avg_posts = avgP.avg_posts()

        return {
            "report": {
                "avg_posts_per_day": avg_posts["avg_posts_per_day"],
                "avg_posts_per_week": avg_posts["avg_posts_per_week"],
                "avg_posts_per_month": avg_posts["avg_posts_per_month"],
                "post_per_day": avgP.post_per_day(),
            },
            "options": {
                "username": self._username,
                "range_days": self._post_scrap._range_days,
                "start_date": self._post_scrap._start_date,
                "end_date": self._post_scrap._end_date,
            },
        }

    def content_report(self):
        c = Content(profile=self._profile, scrap=self._post_scrap)

        cwms = c.caption_word_most_used()

        return {
            "report": {
                "most_common_words": cwms[0],
                "most_common_hashtags": cwms[1],
            },
            "options": {
                "username": self._username,
                "range_days": self._post_scrap._range_days,
                "start_date": self._post_scrap._start_date,
                "end_date": self._post_scrap._end_date,
            },
        }

    def sentiment_comments(self):
        c = Content(profile=self._profile, scrap=self._post_scrap)

        c.senti_comment()
