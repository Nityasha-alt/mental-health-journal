import streamlit as st
import pandas as pd
from datetime import datetime
from mood_utils import detect_mood
from affirmations import get_affirmation
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mental Health Journal", layout="centered")

st.title("🧠 Mental Health Journal")
st.markdown("Write your daily thoughts and track your emotional wellbeing.")

entry = st.text_area("📝 What's on your mind today?", height=200)

if st.button("Submit"):
    if entry.strip() == "":
        st.warning("Please write something before submitting.")
    else:
        mood = detect_mood(entry)
        date = datetime.now().strftime("%Y-%m-%d")

        new_entry = pd.DataFrame([[date, entry, mood]], columns=["Date", "Entry", "Mood"])
        try:
            old = pd.read_csv("entries.csv")
            updated = pd.concat([old, new_entry], ignore_index=True)
        except FileNotFoundError:
            updated = new_entry

        updated.to_csv("entries.csv", index=False)

        st.success(f"Mood detected: **{mood.upper()}**")
        st.info(get_affirmation(mood))

# Mood Trend
if st.checkbox("📊 Show Mood Trend"):
    try:
        data = pd.read_csv("entries.csv")
        st.subheader("Your Mood Frequency")
        mood_counts = data["Mood"].value_counts()
        st.bar_chart(mood_counts)
    except:
        st.warning("No entries yet to show mood chart.")
