from textblob import TextBlob

def detect_mood(text):
    if not text.strip():
        return "neutral"

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    lowered = text.lower()

    # Keyword-based emotion overrides
    sad_keywords = [
        "sad", "cry", "hopeless", "depressed", "alone", "worthless", "tired",
        "anxious", "angry", "frustrated", "upset", "helpless", "lost"
    ]
    happy_keywords = [
        "happy", "joy", "excited", "amazing", "great", "love", "grateful",
        "smile", "peaceful", "energized", "glad"
    ]

    # Keyword override
    if any(word in lowered for word in sad_keywords):
        return "sad"
    if any(word in lowered for word in happy_keywords):
        return "happy"

    # Sentiment-based fallback
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"
