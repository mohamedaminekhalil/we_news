import requests
from datetime import date

API_ENDPOINT = "https://newsapi.org/v2/top-headlines?"
API_KEY = "Your_API_KEY_here"

header = {
    "X-Api-Key": API_KEY
}

params_cat = {
    "pageSize": 15,
    "page": 1,
    "from": date.today(),
    "sortBy": "popularity",
    "country": "us",
    "language": "en",
    "category": ""
}

params_sources = {
    "pageSize": 15,
    "page": 1,
    "sortBy": "publishedAt",
    "language": "en",
    "sources": ""
}

sources = {"entertainment": "buzzfeed,ign,polygon",
           "general": "the-wall-street-journal,abc-news,associated-press,bbc-news,cbc-news,cnn,google-news,nbc-news,"
                      "politico,Reuters,the-washington-post",
           "sports": "four-four-two,talksport,the-sport-bible,fox-sports,bbc-sport,bleacher-report,espn",
           "technology": "wired,techradar,the-next-web,the-verge,techcrunch,ars-technica,engadget,hacker-news,recode"
           }


def clean_content(content):
    return content.split("[+", 1)[0]


def generate_articles(categories):
    """
    Get today articles via api for different categories using sources from the list
    :param categories:
    :return list data:
    """
    data = []
    for category in categories:
        if category in ["science", "health", "business"]:
            params_cat["category"] = category
            req = requests.get(url=API_ENDPOINT, params=params_cat, headers=header)
        else:
            params_sources["sources"] = sources[category]
            req = requests.get(url=API_ENDPOINT, params=params_sources, headers=header)
        if req.json()["status"] == 'ok':
            articles = req.json()["articles"]
            for article in articles:
                if article["urlToImage"] is not None and article["content"] is not None:
                    data.append((category, date.today(), article["title"], clean_content(article["content"]),
                                 article["url"], article["urlToImage"], article["author"], False, False))
    return data
