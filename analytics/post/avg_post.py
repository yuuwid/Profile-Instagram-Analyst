import instaloader
from datetime import datetime, timedelta
from collections import defaultdict

from .posts import PostScrap


class AvgPost:
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

    def avg_posts(self):
        start_date = datetime.now() - timedelta(days=30)

        posts_per_day = defaultdict(int)
        posts_per_week = defaultdict(int)
        posts_per_month = defaultdict(int)

        for post in self._get_30day_post():
            post_date = post["date"]
            if post_date >= start_date:
                posts_per_day[post_date.date()] += 1

                year, week_num, _ = post_date.isocalendar()
                posts_per_week[(year, week_num)] += 1

                year_month = (post_date.year, post_date.month)
                posts_per_month[year_month] += 1

        total_days = (datetime.now() - start_date).days
        total_weeks = total_days // 7
        total_months = total_days // 30

        avg_posts_per_day = sum(posts_per_day.values()) / total_days
        avg_posts_per_week = sum(posts_per_week.values()) / total_weeks
        avg_posts_per_month = sum(posts_per_month.values()) / total_months

        return {
            "avg_posts_per_day": avg_posts_per_day,
            "avg_posts_per_week": avg_posts_per_week,
            "avg_posts_per_month": avg_posts_per_month,
        }

    def post_per_day(self):
        posts_per_date = defaultdict(int)
        start_date = datetime.now() - timedelta(days=30)

        for post in self._get_30day_post():
            post_date = post["date"]
            if post_date >= start_date:
                formatted_date = post_date.strftime("%Y-%m-%d")
                posts_per_date[formatted_date] += 1

        # Fill in dates with 0 posts
        date_range = [start_date + timedelta(days=i) for i in range(30)]
        for date in date_range:
            formatted_date = date.strftime("%Y-%m-%d")
            if formatted_date not in posts_per_date:
                posts_per_date[formatted_date] = 0

        return posts_per_date
