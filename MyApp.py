
import requests
from streamlit_lottie import st_lottie
import streamlit as st

#Emojis can be found on "https://www.webfx.com/tools/emoji-cheat-sheet/" 
st.set_page_config(page_title='Pree Space', page_icon= ":wave:", layout="wide")

def lottieurl_load(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----USE LOCAL CSS----

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>")
    
local_css('style/style.css')

#----LOAD ANIMATIONS----
lottie_coding = lottieurl_load('https://assets6.lottiefiles.com/packages/lf20_zmlg2tee.json')


#----HEADER SECTION-----
with st.container():
    st.header('Namaste :pray:  My name is Preetha')
    st.title('A certified data scientist from India living in China.' )
    st.write('I am curious about everything DATA/ML/AI')
    st.write('[Learn more > ](https://github.com/rajinipreethajohn/Preetha_Portfolio)')
    
#-----WHAT I DO-----
with st.container():
    st.write('----')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write('##')
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')
        
#----CONTACT FORM----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")
    
    #Documentation for FORMS from https://formsubmit.co/. USE YOUR EMAIL ADDRESS
    
    contact_form = """ 
    <form action="https://formsubmit.co/rajinipreethaj@hotmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false"/>
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your E-mail" required>
     <textarea name="message" placeholder = "Your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



