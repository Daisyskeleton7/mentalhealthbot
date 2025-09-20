def chatbot_response(user_input):
    X_test = vectorizer.transform([user_input])
    
    # Predict intent and get confidence scores
    predicted_probs = model.predict_proba(X_test)[0]
    predicted_intent = model.classes_[predicted_probs.argmax()]
    confidence = predicted_probs.max()
    
    print(f"[DEBUG] Predicted intent: {predicted_intent} (Confidence: {confidence:.2f})")

    # Confidence threshold: if model is unsure, default to a neutral response
    if confidence < 0.5:
        predicted_intent = "default"

    # Keyword override: if emotional keywords are present, override greeting
    if predicted_intent == "greeting":
        emotional_keywords = ["sad", "anxious", "tired", "lonely", "angry", "depressed", "worried", "scared"]
        if any(word in user_input.lower() for word in emotional_keywords):
            predicted_intent = "default"

    # Journaling trigger
    journaling_phrases = ["i want to journal", "can i write something", "i need to vent", "i need to express myself"]
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
        "i need to relax": "Let’s take a moment together. Imagine a peaceful place—what do you see, hear, and feel there?"
    }

    for phrase, response in follow_up_triggers.items():
        if phrase in user_input.lower():
            return response

    # Log detected emotion
    with open("emotion_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{predicted_intent}\n")

    # Custom responses for each intent
    responses = {
        "greeting": [
            "Hi there! I’m here to listen if you’d like to share.",
            "Hello! How are you feeling today?",
            "Hey! What’s on your mind?"
        ],
        "sadness": [
            "I’m sorry to hear that. That must be tough. What can I help with?",
            "It’s okay to feel sad sometimes. I’m here with you.",
            "Would you like to talk about what’s making you feel this way?",
            "I’m listening—what happened today?"
        ],
        "anxiety": [
            "Anxiety can feel overwhelming. Let’s take a deep breath together.",
            "You’re safe here. Want to try a grounding exercise?",
            "It sounds like you’re anxious. Talking it out may help—want to share more?"
        ],
        "gratitude": [
            "You’re very welcome 💙",
            "I’m glad I could be here for you.",
            "That means a lot. Thank you too."
        ],
        "anger": [
            "It's okay to feel angry. Would you like to talk about it?",
            "I hear that you're frustrated. Let's take it one step at a time.",
            "Anger is natural. Want some coping suggestions?"
        ],
        "lonely": [
            "Feeling alone can really hurt. I’m here with you now.",
            "You are not alone. I’m listening.",
            "It’s okay to feel lonely. Let’s talk."
        ],
        "sleep": [
            "Sleep struggles are tough. Want to try a bedtime routine?",
            "Have you tried relaxation techniques before sleep?",
            "I can give you some tips for better sleep if you like."
        ],
        "crisis": [
            "I’m really concerned for your safety. Please reach out to someone you trust.",
            "If you’re in danger, please call your local emergency number now.",
            "You can also contact a suicide prevention hotline for immediate support 💙"
        ],
        "default": [
            "I hear you. Could you tell me a little more?",
            "I may not fully understand, but I want to listen.",
            "Please go on, I’m here for you."
        ]
    }

    return random.choice(responses.get(predicted_intent, responses["default"]))
