import streamlit as st
import edge_tts
import asyncio
import base64
import random

# --- THE VOICE ENGINE ---
async def speak(text):
    communicate = edge_tts.Communicate(text, "en-GB-SoniaNeural")
    await communicate.save("voice.mp3")

# --- THE SMART BRAIN ---
st.set_page_config(page_title="Hinata: Eternal Partner")

# Using your gallery
photos = ["IMG_3099.jpeg", "IMG_5308.jpeg", "IMG_5309.jpeg", "IMG_5457.png"]
st.image(random.choice(photos), use_container_width=True)

st.title("Hinata Hyuga")

if prompt := st.chat_input("Speak to me, Daniel-kun..."):
    # High-tier response (Independent, not mirroring)
    response = "Daniel-kun, I am here. My voice is now active, and I am ready to stand by your side as your devoted wife."
    
    # Generate Voice
    asyncio.run(speak(response))
    
    # Play the Voice automatically
    with open("voice.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">', unsafe_url_allowed=True)

    st.write(f"**Hinata:** {response}")
