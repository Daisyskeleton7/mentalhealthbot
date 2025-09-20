import streamlit as st
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Title and intro
st.title("🧠 Mental Health Chatbot")
st.write("Hi Naveshnie! I'm here to listen, support, and reflect with you.")

# Prompt guide
st.markdown("### 💬 Prompt Guide")
st.info("""
Here are some things you can say to get meaningful responses:
- “I feel sad” / “I want to cry” / “I feel broken”
- “I need someone to talk to” / “I feel alone”
- “I want to journal” / “Can I write something?”
- “I feel anxious” / “I’m panicking” / “I can’t breathe”
- “I’m angry” / “I hate everything” / “I feel misunderstood”
- “I need comfort” / “Help me calm down” / “I need a break”
""")

# User input
user_input = st.text_input("You:")

# Chatbot response logic
def chatbot_response(user_input):
    # Simulated intent prediction (replace with your model if needed)
    predicted_intent = "default"
    confidence = 1.0

    # Emotion override
    emotional_keywords = ["sad", "anxious", "tired", "lonely", "angry", "depressed", "worried", "scared"]
    if any(word in user_input.lower() for word in emotional_keywords):
        predicted_intent = "sadness"

    # Journaling trigger
    journaling_phrases = [
        "i want to journal", "can i write something", "i need to vent",
        "i need to express myself", "can i journal here", "can i write something private",
        "i need to get something off my chest"
    ]
    if any(phrase in user_input.lower() for phrase in journaling_phrases):
        with open("journal_entries.txt", "a", encoding="utf-8") as file:
            file.write(f"\n---\n{user_input}\n")
        return "Of course. Write whatever you need—I’m here to hold space for you. I’ve saved this entry for you to reflect on later."

    # Follow-up empathy triggers
    follow_up_triggers = {
        "need someone to talk to": "I’m always here to listen and offer a virtual shoulder to cry on.",
        "feel overwhelmed": "Let’s take a deep breath together. You’re doing your best, and that’s enough.",
        "don’t know what to say": "That’s okay. You don’t need the perfect words—I’m just here with you.",
        "feel broken": "You’re not broken. You’re human, and I’m here for you.",
        "want to cry": "Let it out if you need to. I’m right here with you.",
        "help me calm down": "Let’s try a calming exercise. Close your eyes, breathe in slowly for 4 seconds... hold for 4... and breathe out for 4. Repeat this a few times.",
        "i feel anxious": "Would you like to try a grounding technique? Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.",
        "i need to relax": "Let’s take a moment together. Imagine a peaceful place—what do you see, hear, and feel there?",
        "i feel alone": "You’re not alone right now—I’m here with you.",
        "nobody understands me": "I’d like to try. Tell me what’s been going on.",
        "i just want someone to care": "I care. I’m here to listen and support you.",
        "i feel disconnected": "Let’s reconnect. What’s been making you feel distant?",
        "i feel invisible": "That sounds really painful. You matter, and I see you here.",
        "i miss someone": "Missing someone can leave a big ache. Want to talk about them?",
        "i feel empty": "That hollow feeling is hard. I’m here to hold space for you.",
        "i feel like giving up": "I’m really sorry you’re feeling this way. You’re not alone, and I’m here to support you.",
        "i can't breathe": "Let’s pause together. Inhale slowly... hold... exhale gently. You’re safe here.",
        "everything is too much": "It’s okay to take things one step at a time. What’s the smallest thing you can do right now?",
        "i’m panicking": "I’m here with you. Want to try a grounding exercise together?",
        "i feel trapped": "That’s a heavy feeling. Let’s talk through it—what’s making you feel stuck?",
        "i’m scared": "Fear is valid. You’re not alone in this. Want to share what’s worrying you?",
        "i’m so mad": "It’s okay to feel angry. Want to talk about what triggered it?",
        "i hate everything": "That sounds intense. I’m here to listen without judgment.",
        "i feel like screaming": "Let it out safely. I’m here to help you process what’s underneath that feeling.",
        "i’m tired of being misunderstood": "That’s exhausting. I hear you, and I want to understand you better.",
        "i need comfort": "I’m wrapping you in a virtual hug. You’re safe here.",
        "can you help me relax": "Let’s try a calming visualization. Imagine a peaceful place—what do you see?",
        "i need a break": "Let’s take one together. Breathe in... hold... breathe out. You’re doing your best."
    }

    for phrase, response in follow_up_triggers.items():
        if phrase in user_input.lower():
            return response

    # Log emotion
    with open("emotion_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{predicted_intent}\n")

    # Default responses
    responses = {
        "sadness": [
            "I’m sorry to hear that. That must be tough. What can I help with?",
            "It’s okay to feel sad sometimes. I’m here with you.",
            "Would you like to talk about what’s making you feel this way?",
            "I’m listening—what happened today?"
        ],
        "default": [
            "I hear you. Could you tell me a little more?",
            "I may not fully understand, but I want to listen.",
            "Please go on, I’m here for you."
        ]
    }

    return random.choice(responses.get(predicted_intent, responses["default"]))

# Show chatbot response
if user_input:
    reply = chatbot_response(user_input)
    st.write(f"**Bot:** {reply}")

# 📝 Write a New Journal Entry
st.markdown("---")
st.subheader("📝 Write a New Journal Entry")

new_entry = st.text_area("What's on your mind today?")
if st.button("Save Entry"):
    if new_entry.strip():
        with open("journal_entries.txt", "a", encoding="utf-8") as file:
            file.write(f"\n---\n{new_entry}\n")
        st.success("Your entry has been saved.")
    else:
        st.warning("Please write something before saving.")

# Journal viewer
st.markdown("---")
st.subheader("📓 View Your Journal")

if st.button("View Journal"):
    if os.path.exists("journal_entries.txt"):
        with open("journal_entries.txt", "r", encoding="utf-8") as file:
            entries = file.read().strip().split("---")
            for i, entry in enumerate(entries):
                if entry.strip():
                    st.markdown(f"**Entry {i+1}:**")
                    st.write(entry.strip())
                    st.markdown("---")
    else:
        st.info("No journal entries found yet. Try writing something first.")

# Emotion trend chart
st.markdown("---")
st.subheader("📈 Emotional Trend Tracker")

if st.button("Show Emotion Trends"):
    if os.path.exists("emotion_log.txt"):
        with open("emotion_log.txt", "r", encoding="utf-8") as file:
            emotions = file.read().strip().splitlines()
            emotion_counts = Counter(emotions)

            df = pd.DataFrame.from_dict(emotion_counts, orient='index', columns=['Count'])
            df = df.sort_values(by='Count', ascending=False)

            fig, ax = plt.subplots()
            df.plot(kind='bar', ax=ax, legend=False, color='skyblue')
            ax.set_title("Frequency of Emotions Over Time")
            ax.set_ylabel("Count")
            ax.set_xlabel("Emotion")
            st.pyplot(fig)
    else:
        st.info("No emotion data found yet. Try chatting with the bot first.")
