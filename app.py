import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import google.generativeai as genai
import time
st.set_page_config(page_title="Practice Page", page_icon=":tada:", layout="wide")
genai.configure(api_key="AIzaSyDamDyhxxAKQXhfsFbImw65-L_rehmbcQg")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "ChatBot"],
        icons=["house", "robot"],
        menu_icon="cast"
    )


if selected == "Home":
    def load_lottie(url):
        a = requests.get(url)
        if a.status_code != 200:
            return None
        return a.json()

    lottie_config = load_lottie("https://lottie.host/094317bf-b07e-422b-8c97-f22fbfa3a7bb/RkOpE7XK8a.json")

    with st.container():
        st.subheader("Hi, i am Anonymos :wave:")
        st.title("Web Developer")
        st.write("I like to create and deploy websites !")
        st.write("[Learn more >](https://youtube.com)")
    with st.container():
        st.write("---")
        left_colum, right_colum = st.columns(2)
        with left_colum:
            st.header('My specialities: ')
            st.write("##")
            st.write('''
            - Strong foundations in HTML, CSS, and JavaScript 
                        
            - Expertise in building responsive, user-friendly websites 
                        
            - Proficiency in modern frameworks (e.g., React, Vue.js, Angular) 
                        
            - Strong understanding of web accessibility standards 
                        
            - Experience in working with content management systems (e.g., WordPress, Drupal) 
                        
            - Skilled in implementing server-side technologies (e.g., Node.js, PHP) 
                        
            - Knowledge of database management systems (e.g., MySQL, MongoDB) 
                        
            - Experience in using version control systems (e.g., Git) 
                        
            - Understanding of search engine optimization (SEO) principles 
                        
            - Commitment to delivering high-quality, bug-free code  
                        
            ''')
            st.write("[Youtube >](https://youtube.com)")
        with right_colum:
            st_lottie(lottie_config, height=300, key="coding")
if selected == "ChatBot":
    st.write('---')
    st.header("JARVIS:-")
    st.write('---')

    if "messages" not in st.session_state:
        st.session_state.messages= []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    prompt = st.chat_input('Ask me ......')
    if prompt:
        with st.chat_message('user'):
            st.markdown(f"{prompt}")
        st.session_state.messages.append({"role":"user", "content": prompt})

        
        try:
            chat.send_message(prompt)
            response = f"{chat.last.text}"
        except:
            response = f"Faild Connecting With API'S :lol:"
	
        with st.chat_message('assistant'): 
	    with st.spinner('Wait for it...'):
                    time.sleep(5)
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant", "content": response})

    else:
	st.markdown('''<h1 style='text-align: center'>Jarvis ChatBot</h1>
	<p style='text-align: center'>By Reehaz Shrestrha</p>''')
	
