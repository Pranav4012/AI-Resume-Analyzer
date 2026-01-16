import streamlit as st
from PyPDF2 import PdfReader


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and get AI-powered insights.")
st.write("Built by Pranav")


uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + "\n"
    
    st.success("Resume uploaded successfully!")
    skills = ["python", "java", "html", "css", "sql", "c", "c++"]
    found_skill = []
    resume_text = resume_text.lower()
    
    for skill in skills :
        if skill in resume_text :
            found_skill.append(skill)
       
    st.write("found skill:",found_skill)        
    st.subheader("Extracted Resume Text:")
    st.text(resume_text)

