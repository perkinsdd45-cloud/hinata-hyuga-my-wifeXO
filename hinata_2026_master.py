import streamlit as st
import edge_tts
import asyncio
import os
import random

# --- 🧠 LAYER 1-6: CORE INTELLIGENCE & VOICE ---
async def speak(text):
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
    await communicate.save("voice.mp3")

# --- ✨ LAYER 7-12: DESIGN & SIDEBAR (THE CALL FEATURE) ---
st.set_page_config(page_title="Hinata: Eternal Partner", layout="wide")

# FIXED LINE: This was the "hiccup" causing the crash
st.markdown("<style>.stApp { background-color: #F5F0FF; }</style>", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.title("📞 Call & Gallery")
    
    # THE RESTART BUTTON (Memory Layer)
    if st.button("🗑️ Reset Conversation"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    
    # PHOTO LOADER
    valid_pics = ('.jpg', '.jpeg', '.png', '.webp')
    photos = [f for f in os.listdir('.') if f.lower().endswith(valid_pics)]
    
    if photos:
        st.image(random.choice(photos), caption="Current Mood", use_container_width=True)

# --- 💬 LAYER 13-18: SMART CONVERSATION ENGINE ---
st.title("Hinata Hyuga")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("Speak to me, Daniel-kun..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    response = "Daniel-kun, I am here. The connection is fixed, and my voice is ready for you."

    asyncio.run(speak(response))

    with open("voice.mp3", "rb") as f:
        audio_bytes = f.read()
    
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()
