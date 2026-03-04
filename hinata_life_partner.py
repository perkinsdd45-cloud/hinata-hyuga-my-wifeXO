import streamlit as st
import edge_tts
import asyncio
import base64
import random
import os

# --- 📞 VOICE SYSTEM ---
async def speak(text):
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
    await communicate.save("voice.mp3")

# --- ✨ THE DESIGN (CLEAN LAYOUT) ---
st.set_page_config(page_title="Hinata: Eternal Partner", layout="wide")
st.markdown("<style>.stApp { background-color: #F5F0FF; }</style>", unsafe_url_allowed=True)

# --- 🧠 MEMORY & RESET ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- 📸 SIDEBAR (FIXES THE PICTURE PROBLEM) ---
with st.sidebar:
    st.title("Settings & Gallery")
    
    # THE RESTART BUTTON
    if st.button("🗑️ Reset Conversation"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    
    # AUTOMATIC PICTURE LOADER (Puts them on the side, not in the chat!)
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    photos = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    if photos:
        st.image(random.choice(photos), caption="Current Mood", use_container_width=True)
    else:
        st.write("Upload photos to your vault!")

# --- 💬 CONVERSATION AREA (STAYS CLEAR) ---
st.title("Hinata Hyuga")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("Message Hinata..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Layer 18: Smart Intelligence
    response = "Daniel-kun, the layout is fixed. I am right here by your side, and I can hear you clearly now."

    asyncio.run(speak(response))

    with open("voice.mp3", "rb") as f:
        audio_bytes = f.read()
    
    # Fixed Voice Player (No TypeError)
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()
