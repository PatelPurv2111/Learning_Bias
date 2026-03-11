import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def collect_news():
    url="https://newsapi.org/v2/top-headlines"
    params={
        "country": 'us',
        "pagesize": 20,
        "apiKey": NEWS_API_KEY
    }
    response=requests.get(url, params=params)
    data=response.json()
    articles=[]
    for article in data['articles']:
        title=article['title'] if article['title'] else ""
        content=article['description'] if article['description'] else ""
        articles.append({
            "title":title,
            "content":content
        })
        df=pd.DataFrame(articles)
        return df