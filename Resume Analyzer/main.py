import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()   
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📃", layout="centered")
st.title("AI Resume Analyzer")
st.markdown("Upload your Resume and get a AI powered analysis of your resume!")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
uploaded_file = st.file_uploader("Upload your Resume(PDF or TXT file)", type=["pdf", "txt"])
job_role = st.text_input("Enter the Job Role you are looking for")
analyze= st.button("Analyze Resume")
def extract_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file is not None:
    st.write("Analyzing Resume...")
    try:
        content=extract_file(uploaded_file)
        if not content.strip():
            st.error("File doesnt have any content!")
            st.stop()
        prompt=f"""Please analyze the content of the resume and provide me with constructive feedback. I want you to focus on following aspects:
        1. Clarity of content and it's impact
        2. Skills Presentation
        3. Experience Description
        4. Make sure there is no inappropriate words
        5. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {content}
        Please provide analysis in a structured format and need for changes and it's reasons        
"""
        client=genai.Client(GOOGLE_API_KEY)
        response=client.chat.completions.create(
            model='gemini-2.5-pro',
            messages=[
                {
                    "role": "You are an expert resume analyzer, with decades of experience in HR and Recruitment department",
                    "content": prompt
                }],
            temperature=0.7,
            max_output_tokens=1000
        )
        st.markdown("#Analyzis Result#")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello, how are you?")