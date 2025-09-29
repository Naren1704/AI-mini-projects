# AI-mini-projects
This repository contains three AI-powered mini projects built using Python, LangChain, TensorFlow/Keras, Streamlit, and Google Generative AI (Gemini). Each project demonstrates how AI can be used in different domains — conversational agents, computer vision, and text analysis for resumes.

Projects Included
1. AI Chatbot with Tool Integration
A conversational AI assistant powered by LangChain, Google Generative AI (Gemini), and custom tools.

* Features:

Interactive chatbot that responds to user queries

Integrated with custom tools like add(a, b) for arithmetic operations and greet(name) for personalized greetings

Uses create_react_agent from LangGraph to enable ReAct-style reasoning

Supports real-time streaming responses

* Run Instructions:

python chatbot.py
Type your queries in the terminal. Type quit to exit.

2. AI Image Classifier
A Streamlit web app that uses a pre-trained MobileNetV2 CNN model (ImageNet) to classify uploaded images.

* Features:

Upload images in .jpg, .jpeg, or .png format

Top 3 predictions with confidence scores

Simple and easy-to-use web interface

* Run Instructions:

streamlit run image_classifier.py
Open the provided local URL in your browser, upload an image, and classify it.

3. AI Resume Analyzer
A Streamlit-based resume analyzer powered by Gemini (Google Generative AI).

* Features:

Upload resumes in PDF or TXT format

Extracts and analyzes resume content automatically

Provides detailed feedback on clarity, skills presentation, experience, and improvements tailored to job roles

Ensures professional and constructive suggestions

* Run Instructions:

streamlit run resume_analyzer.py
Upload your resume file, enter a target job role, and click Analyze Resume.

* Requirements
Ensure you have the following installed before running the projects:

Python 3.9+
Required libraries (install via requirements.txt):
pip install -r requirements.txt
Key Dependencies
langchain
langchain-core
langchain-google-genai
langgraph
google-generativeai
streamlit
tensorflow
opencv-python
pillow
PyPDF2
numpy
python-dotenv

* Environment Setup
Create a .env file in the root directory.

* Add your Google API key:

GOOGLE_API_KEY=your_api_key_here
Folder Structure

📂 ai-mini-projects
 ├── chatbot.py            # AI chatbot with LangChain & Gemini
 ├── image_classifier.py   # Streamlit-based image classifier
 ├── resume_analyzer.py    # Resume analyzer app using Gemini
 ├── requirements.txt      # Dependencies
 └── README.md             # Project documentation
Future Improvements
Extend the chatbot to support more tools (weather, knowledge retrieval, etc.)

Improve image classifier with more models and custom training

Add resume keyword matching against job descriptions

