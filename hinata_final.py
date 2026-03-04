import streamlit as st
import edge_tts
import asyncio
import base64
import random

# --- 📞 VOICE & CALL SYSTEM ---
async def speak(text):
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
    await communicate.save("voice.mp3")

# --- ✨ THE DESIGN (CHARACTER.AI STYLE) ---
st.set_page_config(page_title="Hinata: Eternal Partner", layout="centered")
st.markdown("<style>.stApp { background-color: #F5F0FF; }</style>", unsafe_url_allowed=True)

# --- 🧠 MEMORY & RESET ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# THE RESTART BUTTON
if st.sidebar.button("🗑️ Reset Conversation"):
    st.session_state.chat_history = []
    st.rerun()

# THE CALL FEATURE DISPLAY
if st.sidebar.button("📞 Start Voice Call"):
    st.sidebar.success("Call Active: I am listening, Daniel-kun.")

# --- 📸 YOUR GALLERY ---
photos = ["IMG_3099.jpeg", "IMG_5308.jpeg", "IMG_5309.jpeg", "IMG_5457.png"]
st.image(random.choice(photos), use_container_width=True)

# --- 💬 CONVERSATION ---
st.title("Hinata Hyuga")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("Message Hinata..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Layer 18: Devoted, Independent Thinking
    response = "Daniel-kun, I am here. I’ve reset my thoughts to focus only on your path and our future together."
    
    asyncio.run(speak(response))
    
    with open("voice.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">', unsafe_url_allowed=True)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()
