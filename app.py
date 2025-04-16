import streamlit as st
import os
from dotenv import load_dotenv
from pages.login import login_page, load_session_state
from pages.signup import signup_page
from pages.forgot_password import forgot_password_page
from pages.home import home_page
from pages.code_editor import code_editor_page
from pages.chatbot import chatbot_page
import time

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="AI Code Assistant",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stTextInput>div>div>input {
        background-color: #2D2D2D;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Initialize session state with persistent values
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "login"
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'last_activity' not in st.session_state:
        st.session_state.last_activity = time.time()
    if 'remember_me' not in st.session_state:
        load_session_state()  # Try to load saved session state

    # Check for session timeout (30 minutes) if remember me is not checked
    if st.session_state.authenticated and not st.session_state.get('remember_me', False):
        if time.time() - st.session_state.last_activity > 1800:  # 30 minutes
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.current_page = "login"
            st.session_state.remember_me = False
        else:
            st.session_state.last_activity = time.time()

    # Navigation
    if not st.session_state.authenticated:
        if st.session_state.current_page == "login":
            login_page()
        elif st.session_state.current_page == "signup":
            signup_page()
        elif st.session_state.current_page == "forgot_password":
            forgot_password_page()
    else:
        if st.session_state.current_page == "home":
            home_page()
        elif st.session_state.current_page == "code_editor":
            code_editor_page()
        elif st.session_state.current_page == "chatbot":
            chatbot_page()

if __name__ == "__main__":
    main() 