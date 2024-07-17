import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import google.generativeai as genai
import time

# Page configuration
st.set_page_config(page_title="Practice Page", page_icon=":tada:", layout="wide")

# Configure GenerativeAI model
genai.configure(api_key="your_api_key_here")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Sidebar option menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "ChatBot"],
        icons=["house", "robot"],
        menu_icon="cast"
    )

# Main content based on selected option
if selected == "Home":
    def load_lottie(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error loading Lottie animation: {e}")
            return None
    
    # Load Lottie animation
    lottie_config = load_lottie("https://lottie.host/094317bf-b07e-422b-8c97-f22fbfa3a7bb/RkOpE7XK8a.json")

    # Home page layout
    st.subheader("Hi, I am Anonymos :wave:")
    st.title("Web Developer")
    st.write("I like to create and deploy websites!")
    st.write("[Learn more >](https://youtube.com)")

    st.write("---")

    # Columns for specialities
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('My specialties:')
        st.write('''
        - Strong foundations in HTML, CSS, and JavaScript 
        - Expertise in building responsive, user-friendly websites 
        - Proficiency in modern frameworks (e.g., React, Vue.js, Angular) 
        - Strong understanding of web accessibility standards 
        - Experience in working with content management systems (e.g., WordPress, Drupal) 
        ''')
        st.write("[Youtube >](https://youtube.com)")

    with right_column:
        st_lottie(lottie_config, height=300, key="coding")

elif selected == "ChatBot":
    st.write('---')
    st.header("JARVIS:-")
    st.write('---')

    # Initialize or load chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input prompt for user
    prompt = st.chat_input('Ask me ......')

    # Process user input and generate response
    if prompt:
        with st.chat_message('user'):
            st.markdown(f"{prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Send user message to GenerativeAI model
        try:
            chat.send_message(prompt)
            response = f"{chat.last.text}"
        except Exception as e:
            response = f"Failed Connecting With APIs: {e}"

        # Display assistant's response with spinner
        with st.spinner('Wait for it...'):
            time.sleep(2)  # Simulate processing delay
            with st.chat_message('assistant'):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    else:
        st.markdown('''
        ## Jarvis ChatBot
        By Reehaz Shrestrha
        ''')
