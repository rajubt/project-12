import streamlit as st
import google.generativeai as genai

api_key = st.secrets['google_api_key']
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)

with col1:
    st.subheader('Hello :wave:')
    st.title('lets start')

with col2:
    st.image('images/Designer (1).png')

st.write(' ')

persona = '''
hi, you help pepole asnwer question about your self (i.e. kaustab)  my name is kaustab i am 24 yraes old i live in delhi'''
st.title('My AI Bot')
st.write('ask anything about me')

user_ques = st.text_input('hi there')
if st.button('ask',use_container_width=400):
    prompt = persona + 'here is the question that user ask:' + user_ques
    response = model.generate_content(prompt)
    st.title(response.text)




col1, col2 = st.columns(2)

with col1:
    st.video('https://youtu.be/4iiLuQVMs-w?si=MLoleCjUzbeRObqV')


# st.title('My Skills')
#
# st.slider('programming',0,100,70)
# st.slider('teaching',0,100,70)
# st.slider('playing',0,100,70)
# st.slider('prob silving',0,100,70)
# st.slider('driving',0,100,70)
# st.slider('swimming',0,100,70)
# st.file_uploader('upload a file')
#
#
# st.title('gallery')
#
# col1,col2,col3 = st.columns(3)
# with col1:
#      st.image('images/Designer (1).png')
#      st.image('images/Designer (1).png')
#      st.image('images/Designer (1).png')
#
#
#
#
#
# with col2:
#     st.image('images/Designer (1).png')
# with col3:
#     st.image('images/Designer (1).png')