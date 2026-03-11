from textblob import TextBlob
def analyze_sentiment(text):
    polarity=TextBlob(text).sentiment.polarity
    
    if polarity>0:
        return "Positive"
    if polarity<0:
        return "Negative"
    return "Neutral"