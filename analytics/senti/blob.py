from textblob import TextBlob


def senti(text):
    analysis = TextBlob(text)
    sentiment_polarity = analysis.sentiment.polarity

    # Classify
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity == 0:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    return sentiment_polarity, sentiment
