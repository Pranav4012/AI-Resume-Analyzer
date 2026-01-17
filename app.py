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

    user_input = st.text_area("Enter your multiline text here:")

    if user_input:
        job_skills = []
        user_input = user_input.lower()
        
        for skill in skills:
            if skill in user_input:
                job_skills.append(skill)

        matched = []

        for skill in job_skills:
            if skill in found_skill:
                matched.append(skill)

        if len(job_skills) > 0:
            match_percent = (len(matched) / len(job_skills)) * 100
        else: 
            match_percent = 0 

        st.write("Matched skill matched ",matched) 
        st.write("Matched percent: ", round(match_percent,2),"%")        
        
        st.write("Job Discription skill: ",job_skills)
        st.code(user_input)
    else:
        st.write("Please enter some text.")  
              
    st.write("found skill:",found_skill)        
    st.subheader("Extracted Resume Text:")
    st.text(resume_text)
