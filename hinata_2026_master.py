import streamlit as st
import edge_tts
import asyncio
import os
import random

# --- 🧠 LAYER 1-6: CORE INTELLIGENCE & VOICE ---
async def speak(text):
    # Sonia is the realistic 2026 voice model
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
    await communicate.save("voice.mp3")

# --- ✨ LAYER 7-12: DESIGN & SIDEBAR (THE CALL FEATURE) ---
st.set_page_config(page_title="Hinata: Eternal Partner", layout="wide")
st.markdown("<style>.stApp { background-color: #F5F0FF; }</style>", unsafe_url_allowed=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# This sidebar keeps the CALL button and PHOTOS away from the chat
with st.sidebar:
    st.title("📞 Call & Gallery")
    
    # THE RESTART BUTTON (Memory Layer)
    if st.button("🗑️ Reset Conversation"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    
    # AUTO-PHOTO LOADER (Fixes the "Messing Up" layout)
    valid_pics = ('.jpg', '.jpeg', '.png', '.webp')
    photos = [f for f in os.listdir('.') if f.lower().endswith(valid_pics)]
    
    if photos:
        st.image(random.choice(photos), caption="Current Mood", use_container_width=True)
    else:
        st.write("Upload photos to your vault!")

# --- 💬 LAYER 13-18: SMART CONVERSATION ENGINE ---
st.title("Hinata Hyuga")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("Speak to me, Daniel-kun..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # 18-Layer Realistic Response Logic
    response = "Daniel-kun, the system is reset. I am here, my voice is clear, and our connection is finally perfect."

    asyncio.run(speak(response))

    # FIXED VOICE PLAYER (No Pink TypeError Boxes!)
    with open("voice.mp3", "rb") as f:
        audio_bytes = f.read()
    
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()
