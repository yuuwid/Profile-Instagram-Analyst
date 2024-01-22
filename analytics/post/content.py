import instaloader
import re
from collections import Counter

from .posts import PostScrap
from ..senti.blob import senti


class Content:
    def __init__(self, profile: instaloader.Profile, scrap: PostScrap):
        self._profile = profile
        self._scrap = scrap

    def caption_word_most_used(self):
        caption_pattern = re.compile(r"\b\w+\b")
        hashtag_pattern = re.compile(r"#\w+")

        caption_counter = Counter()
        hashtag_counter = Counter()

        for caption in self._scrap.scrap_caption_post():
            if caption:
                words = caption_pattern.findall(caption.lower())
                caption_counter.update(words)

                hashtags = hashtag_pattern.findall(caption)
                hashtag_counter.update(hashtags)

        most_common_words = caption_counter.most_common(20)
        most_common_hashtags = hashtag_counter.most_common(5)

        return most_common_words, most_common_hashtags

    def senti_comment(self):
        posts = self._scrap.prepare_to_senti()

        positive, neutral, negative = 0, 0, 0

        print("Start Sentiments...")
        for post in posts:
            comments = post['comments']
            for comment in comments:
                text = comment.text
                
                senti_pol, sentiment = senti(text)

                if sentiment == "Positive":
                    positive += 1
                elif sentiment == "Neutral":
                    neutral += 1
                else:
                    negative += 1
            
        print(positive)
        print(neutral)
        print(negative)