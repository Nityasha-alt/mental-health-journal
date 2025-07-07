def get_affirmation(mood):
    affirmations = {
        "happy": "Keep riding the wave of positivity!",
        "sad": "You are stronger than you think. Tomorrow is a new day.",
        "neutral": "Every step you take matters. Stay grounded."
    }
    return affirmations.get(mood, "You're doing great. Take it one step at a time!")
