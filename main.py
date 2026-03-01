# main.py
import streamlit as st
import time
from app.memory.session_memory import initialize_memory, add_message, get_chat_history
from app.services.chatbot_service import ChatbotService

st.set_page_config(page_title="SoulSupport – Your Emotional Companion")

# -------------------- GLASSMORPHISM UI --------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #1e1e2f, #2c3e50);
    color: white;
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 10px;
    backdrop-filter: blur(10px);
}

/* User bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(0, 123, 255, 0.25);
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: rgba(255, 255, 255, 0.1);
}

/* Input box */
textarea {
    border-radius: 10px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.05);
}

/* Buttons */
button {
    border-radius: 10px !important;
    transition: 0.3s ease-in-out;
}

button:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# -------------------- INITIALIZE --------------------
initialize_memory()
chatbot = ChatbotService()

st.title("🤍 SoulSupport – Your Emotional Companion")
st.caption("A safe space to talk. You're not alone.")

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.title("🌿 About")
    st.write("AI-powered mental health support chatbot.")
    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.clear()
        st.rerun()

# -------------------- CRISIS DETECTION --------------------
CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "i want to die",
    "i don't want to live",
    "end my life",
    "self harm",
    "hurt myself"
]

def is_crisis(text):
    text = text.lower()
    return any(keyword in text for keyword in CRISIS_KEYWORDS)

# -------------------- MOOD EMOJI FUNCTION --------------------
def add_emoji(text):
    text_lower = text.lower()
    if "sad" in text_lower:
        return "💙 " + text
    if "happy" in text_lower:
        return "😊 " + text
    if "anxious" in text_lower or "anxiety" in text_lower:
        return "🌿 " + text
    if "overthinking" in text_lower:
        return "🧠 " + text
    return text

# -------------------- WELCOME MESSAGE --------------------
if len(get_chat_history()) == 0:
    with st.chat_message("assistant"):
        st.markdown("Hi 👋 I'm here to support you. You can share anything you're feeling today.")

# -------------------- DISPLAY CHAT HISTORY --------------------
for message in get_chat_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- USER INPUT --------------------
user_input = st.chat_input("How are you feeling today?")

if user_input:
    add_message("user", user_input)

    with st.chat_message("assistant"):

        # 🚨 CRISIS MODE
        if is_crisis(user_input):

            st.error("🚨 I'm really glad you told me. You don't have to go through this alone.")

            st.markdown("""
                        If you're in immediate danger, please call your local emergency number right now.
                        You deserve support, and there are people ready to help you.
                        """)

            st.markdown("Are you safe right now?")

            add_message("assistant", "Crisis support message displayed.")

        # 💬 NORMAL MODE
        else:
            with st.spinner("Thinking..."):
                response = chatbot.get_response(user_input)

                combined_response = " ".join(
                    response.get(part, "") for part in
                    ["empathy", "prompt", "suggestion", "encouragement"]
                ).strip()

                combined_response = add_emoji(combined_response)

                # Typing animation
                message_placeholder = st.empty()
                full_response = ""

                for word in combined_response.split():
                    full_response += word + " "
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.02)

                message_placeholder.markdown(full_response)

                add_message("assistant", combined_response)

# -------------------- CRISIS SUPPORT FOOTER --------------------
st.markdown("---")
st.info("If you're in immediate danger or need urgent help, please contact your local emergency number or a 24/7 crisis helpline.")