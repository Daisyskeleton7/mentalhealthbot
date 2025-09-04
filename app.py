import streamlit as st
import random
from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Response templates
responses = {
    "POSITIVE": [
        "That's wonderful to hear! What made today feel good?",
        "I'm so glad you're feeling positive. Keep it going!"
    ],
    "NEGATIVE": [
        "I'm really sorry you're feeling this way. You're not alone.",
        "That sounds tough. Want to talk about it more?"
    ],
    "NEUTRAL": [
        "Thanks for sharing. I'm here to listen.",
        "Let's explore that together. What’s been on your mind?"
    ]
}

# Streamlit UI
st.title("🧠 Mental Health Chatbot")
st.write("Hi Naveshnie! I'm here to talk. Type something below:")

user_input = st.text_input("You:")

if user_input:
    sentiment = sentiment_analyzer(user_input)[0]['label']
    reply = random.choice(responses.get(sentiment, responses["NEUTRAL"]))
    st.write(f"**Bot:** {reply}")
