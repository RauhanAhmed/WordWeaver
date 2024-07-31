from textblob import TextBlob

def getSentimentAnalysis(text: str) -> dict[str, float]: 
    text = TextBlob(text)
    polarityScore, subjectivityScore = text.sentiment.polarity, text.sentiment.subjectivity
    if polarityScore < 0:
        polarity = "Negative"
    elif polarityScore > 0:
        polarity = "Positive"
    else:
        polarity = "Neutral"
    return {
        "polarity": polarity,
        "polarityScore": polarityScore,
        "subjectivityScore": subjectivityScore
    }