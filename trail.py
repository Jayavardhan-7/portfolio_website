import google.generativeai as genai
genai.configure(api_key="AIzaSyDd4kBxpk_wUcRsym7PugAyx9RR01VAbrQ")
model=genai.GenerativeModel("gemini-1.5-flash")
response=model.generate_content("What is java?")