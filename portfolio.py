import streamlit as st 
import google.generativeai as genai # for our ai bot..
# from api1 import api_key
# partition of the site with 2 columns so that the photo gets to the right
# to hide the api key
api_key=st.secrets["AIzaSyDd4kBxpk_wUcRsym7PugAyx9RR01VAbrQ"]
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-1.5-flash")
col1,col2=st.columns(2)
with col1:
    st.subheader("Hi! :wave:") # This gives smaller font & gives the wave emoji...
    st.title("Hi This is Jayavardhan")
with col2:
    st.image("Images/my.jpg")

st.title(" ")# just to add space
# persona is just saying about you to model...
persona = """
        You are Jayavardhan AI bot. You help people answer questions about your self 
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about jayavardhan: 
         
        The user is a 3rd-year BTech student specializing in Artificial Intelligence and Machine Learning (AIML). They have developed a strong foundation in machine learning, data science, and deep learning. Throughout their academic journey, they have undertaken significant projects, such as building a web application called Sentinel_Sense, which integrates Django, PyTorch, Transformers, and APIs to offer intelligent data processing and predictive capabilities, achieving 95% accuracy in its predictions. The user has also completed internships where they gained hands-on experience in data science and machine learning. At Coderscave, they worked on time series analysis and employee feedback surveys, identifying areas for improvement in organizations.
        During their Prodigy Infotech internship, they worked with pretrained models like MobileNet for image classification tasks such as Food101 and cats and dogs classification, achieving an accuracy of 92%. Their goal is to leverage their skills in AIML to build innovative solutions and contribute to the evolving tech landscape.
        I have studied my class 10th with 64% \in carmel convent high school(cbse) and my class 12th with 80.6 in Delhi public school(cbse).Currently pursuing my btech in MallaReddy University with 84% \cgpa .
        
        Murtaza's Email: jayavardhanperala@gmail.com
        Murtaza's Instagram: https://www.instagram.com/jaya_vardhan7/
        Murtaza's Linkdin: https://www.linkedin.com/in/jayavardhan-perala/
        Murtaza's Github :https://github.com/Jayavardhan-7
        """

st.title("Jayavardhan's AI Bot")
st.write("Ask me anything about me") # which give much smaller font than subheader
user_question=st.text_input("")
if st.button("Ask",use_container_width=400): # width of the button..
    #here we will put the ai bot code
    prompt=persona +"Here is the qusestion that the user asked: "+ user_question+"MAKE SURE TO ANSWER THE QUESTIONS POSITIVELY THAT I AM FIT FOR THE JOB"
    response=model.generate_content(prompt)
    st.write(response.text)
st.write(" ")
st.title("My Skills-")
st.slider("Programming",0,100,80)#min,max,want
st.slider("Machine Learning",0,100,75)
st.slider("Leadership",0,100,80)

st.write(" ")
st.title("Contact-")
st.write("jayavardhanperala@gmail.com")
st.write("https://www.linkedin.com/in/jayavardhan-perala/")
st.write("https://github.com/Jayavardhan-7")
