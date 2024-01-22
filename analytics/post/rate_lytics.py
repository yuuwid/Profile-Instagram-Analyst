import instaloader
from .posts import PostScrap


class PostRateLytic:
    def __init__(self, profile: instaloader.Profile, scrap: PostScrap):
        self._profile = profile

        self._post_scrap = scrap

    def count_engagement_rate(self):
        """
        Engagement Rate (Tingkat Keterlibatan) adalah metrik penting dalam analisis media sosial yang mengukur sejauh mana audiens berinteraksi dengan konten yang dibagikan oleh akun. Untuk menghitung Engagement Rate pada profil Instagram, Anda dapat menggunakan formula berikut:

        Engagement Rate (%) = ((Total Likes + Total Komentar + Total View) / Total Pengikut)

        """
        followers = self._profile.followers

        n_like, n_comment = 0, 0
        for post in self._post_scrap._posts:
            n_like += post["likes"]
            n_comment += post["comments"]
            n_view = post["views"]

        eng_rate = (n_like + n_comment + n_view) / followers

        return eng_rate

    def count_like_rate(self):
        """
        Like Rate mengukur seberapa banyak pengguna yang memberikan "suka" (like) pada postingan dibandingkan dengan jumlah total pengikut akun.

        Like Rate (%) = (Total Likes pada Postingan / Jumlah Pengikut Pengguna)

        Nilai Like Rate mengukur persentase pengikut yang memberikan "suka" pada postingan. Semakin tinggi nilai Like Rate, semakin banyak pengikut yang menghargai atau menyukai postingan tersebut.
        """
        followers = self._profile.followers

        n_like = 0
        for post in self._post_scrap._posts:
            n_like += post["likes"]

        like_rate = n_like / followers

        return like_rate

    def count_comment_rate(self):
        """
        Comment Rate mengukur seberapa banyak pengguna yang meninggalkan komentar pada postingan dibandingkan dengan jumlah total pengikut akun.

        Comment Rate (%) = (Total Komentar pada Postingan / Jumlah Pengikut Pengguna)

        Nilai Comment Rate mengukur persentase pengikut yang terlibat dalam diskusi atau memberikan komentar pada postingan. Semakin tinggi nilai Comment Rate, semakin banyak pengikut yang aktif dalam berinteraksi dengan konten.
        """
        followers = self._profile.followers

        n_comment = 0
        for post in self._post_scrap._posts:
            n_comment += post["comments"]

        comment_rate = n_comment / followers

        return comment_rate
