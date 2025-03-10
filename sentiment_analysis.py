import requests
from textblob import TextBlob
from bs4 import BeautifulSoup

def analyze_sentiment(username):
    url = f"https://nitter.net/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tweets = [tweet.text for tweet in soup.find_all("p")[:5]]
        sentiments = [TextBlob(tweet).sentiment.polarity for tweet in tweets]
        avg_sentiment = sum(sentiments) / len(sentiments)

        if avg_sentiment > 0:
            return f"{username} has a Positive Online Presence."
        elif avg_sentiment < 0:
            return f"{username} has a Negative Online Presence."
        else:
            return f"{username} has a Neutral Online Presence."
    
    return "User not found or private account."
