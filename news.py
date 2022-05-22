import json
import requests


class News:

    def __init__(self, img_url, news_url, title, desc):
        self.img_url = img_url
        self.news_url = news_url
        self.title = title
        self.desc = desc

    def __str__(self):
        return "{title}\n{url}\n{img}\n{desc}".format(title=self.title, url=self.news_url, img=self.img_url, desc=self.desc)


class NewsFetcher:

    api_link = "https://newsapi.org/v2/top-headlines"
    api_key = "ad7356ab087a453a9b7b9aae4a9482f7"
    language = "en"
    category = "business"

    def __init__(self):
        self.fetch_link = "{link}?category={category}&apiKey={key}&language={lang}".format(link=self.api_link, category=self.category, key=self.api_key, lang=self.language)
        self.text = ""
        self.newsfeed = []

    def fetch(self):
        response = requests.get(self.fetch_link)
        if response.status_code == 200:
            self.text = response.text
        else:
            print("Failed to fetch. The server returned {}.".format(response.status_code))

    def load_news(self):
        text = json.loads(self.text)
        for i in range(6):
            img_url = text["articles"][i]["urlToImage"]
            news_url = text["articles"][i]["url"]
            title = text["articles"][i]["title"]
            desc = text["articles"][i]["description"]
            piece = News(img_url=img_url, news_url=news_url, title=title, desc=desc)
            self.newsfeed.append(piece)








