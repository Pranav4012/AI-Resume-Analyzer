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

    if user_input: # creating an empty set for keeping the missing data of user input resume 
        job_skills = []
        user_input = user_input.lower()
        
        for skill in skills:
            if skill in user_input:
                job_skills.append(skill)

        matched = []

        for skill in job_skills:
            if skill in found_skill:
                matched.append(skill)
#for calculating the percentage for job matching 
        if len(job_skills) > 0:
            match_percent = (len(matched) / len(job_skills)) * 100
        else: 
            match_percent = 0 

        missing_skills = []

        for skill in job_skills:
            if skill not in found_skill:
                missing_skills.append(skill)
        
        st.header("Analysis result")
        st.subheader("Match Percent")
        st.write(f"{round(match_percent,2)}%")

        if match_percent > 70 :
            st.success("Great match! Your resume fits this job well.")
        else:
            st.warning("This resume needs improvement for this job.")
        # adding a better way to represent my web page 
        st.subheader("Job Description Skills")
        st.write(job_skills)
        st.subheader("Matched Skills")
        st.write(matched)

        if missing_skills: 
             # this is for checking resume that which skill is missing and will depict it 
            st.subheader("Missing skills")
            st.write(missing_skills) 
        else:
            st.success("You already have all the required skills for this job!")
            st.code(user_input)       
        st.subheader("Job description")
        st.code(user_input)
    else:
        st.write("Please enter some text.")

        #for resume skills and resume text 
    st.subheader("Resume Skills")          
    st.write(found_skill)        
    st.subheader("Extracted Resume Text:")
    st.text(resume_text)