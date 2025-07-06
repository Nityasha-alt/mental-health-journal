import openai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_affirmation(mood):
    prompt = f"Give me one short, motivational affirmation for someone feeling {mood} today."

    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return res.choices[0].message.content.strip()
    except:
        return "You're doing great. Take it one step at a time!"
