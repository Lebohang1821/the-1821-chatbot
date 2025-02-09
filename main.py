import streamlit as st
from datetime import datetime, timedelta
import sys

try:
    import streamlit as st
except ModuleNotFoundError:
    sys.exit("Error: The 'streamlit' module is not installed. Please install it using 'pip install streamlit'.")

from utils import load_chat_history, save_chat_history, generate_ai_response, build_prompt, display_typing_effect

# Load chat history
chat_history = load_chat_history()

# Page Configuration
st.set_page_config(page_title="AI Assistant", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    body { background-color: #121212; color: #FFFFFF; }
    .stChatInput > div { display: flex; gap: 10px; }
    .stChatInput > div > button { background-color: #444; color: white; border-radius: 8px; padding: 8px 15px; }
    .modern-container { text-align: center; margin-top: 20px; }
    .modern-title { font-size: 2.5em; font-weight: bold; }
    .modern-footer { text-align: center; padding: 20px; font-size: 0.9em; color: #bbb; position: fixed; bottom: 0; width: 100%; background: #222; }
    </style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown("""
    <div class='modern-container'>
        <h1 class='modern-title'>Welcome to Your AI Assistant</h1>
    </div>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.image("logo.png", use_container_width=True)
    
    st.header("📜 Chat History")
    
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    categorized_chats = {"Today": [], "Yesterday": [], "Previous 7 Days": []}
    
    for chat in chat_history:
        chat_date = datetime.strptime(chat["date"], "%Y-%m-%d").date()
        if chat_date == today:
            categorized_chats["Today"].append(chat)
        elif chat_date == yesterday:
            categorized_chats["Yesterday"].append(chat)
        elif chat_date >= today - timedelta(days=7):
            categorized_chats["Previous 7 Days"].append(chat)
    
    for category, chats in categorized_chats.items():
        if chats:
            st.subheader(category)
            for chat in chats:
                if st.button(f"🗨️ {chat['title']}", key=chat['title']):
                    st.session_state.message_log = chat['content']

    st.header("🔧 Features")
    notes = st.text_area("Write your notes here...")
    if st.button("Save Note"):
        st.session_state.notes = notes
        st.success("Note saved!")
    
    st.header("⚙️ Configuration")
    with st.expander("Model Selection"):
        selected_model = st.selectbox(
            "Choose Model",
            ["gemini-1.5-pro", "gemini-1.5-flash"],
            index=0
        )

# Chat Interface Logic
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "AI", "content": "How can I assist you today? 😊"}]

for message in st.session_state.message_log:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_query = st.chat_input("Type your message here...")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)
    
    with st.spinner("🔄 Please wait..."):
        prompt_text = build_prompt()
        ai_response = generate_ai_response(prompt_text, selected_model)
    
    st.session_state.message_log.append({"role": "ai", "content": ""})
    display_typing_effect(ai_response)
    st.session_state.message_log[-1]["content"] = ai_response
    chat_history.append({"title": user_query[:30], "content": st.session_state.message_log, "date": datetime.now().strftime("%Y-%m-%d")})
    save_chat_history(chat_history)
    st.rerun()

# Footer
st.markdown("""
    <div class='modern-footer'>
        <p>Powered by Gemini | Designed by 1821</p>
    </div>
""", unsafe_allow_html=True)
