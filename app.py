import streamlit as st
from PIL import Image

# Load assets
logo = Image.open("assets/logo.png")
image1 = Image.open("assets/image1.jpg")
image2 = Image.open("assets/image2.jpg")

# Apply custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Logo and Title
st.image(logo, width=120)
st.title("STEMicolon")
st.subheader("Where science meets hope 💜")

# Mission Statement
st.markdown("""
Welcome to **STEMicolon**, a space for young dreamers who love STEM but feel held back by self-doubt or mental health struggles.

We believe:
- Your GPA doesn’t define your genius.
- Mental health doesn’t cancel your dreams.
- Small steps count — one day, one project, one talk.

Follow us on Instagram [@stemicolon2025](https://www.instagram.com/stemicolon2025) 💫
""")

# Gallery
st.header("🌟 Inspiration Wall")
st.image(image1, caption="You're not alone", use_column_width=True)
st.image(image2, caption="Grades don’t define your genius", use_column_width=True)

# Contact
st.header("📬 Get Involved")
st.markdown("""
Want to share your story, volunteer, or collaborate?

📧 Email: stemicolon2025@gmail.com  
📱 Instagram: [@stemicolon2025](https://www.instagram.com/stemicolon2025)
""")
