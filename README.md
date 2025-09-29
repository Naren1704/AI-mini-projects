🚀 AI Mini Projects

This repository contains three AI-powered mini projects built using Python, LangChain, TensorFlow/Keras, Streamlit, and Google Generative AI (Gemini).
Each project demonstrates how AI can be applied across domains — conversational agents, computer vision, and resume text analysis.

📌 Projects Included
1️⃣ AI Chatbot with Tool Integration

A conversational AI assistant powered by LangChain, Google Generative AI (Gemini), and custom tools.

✨ Features:

Interactive chatbot that responds to user queries

Integrated with tools like add(a, b) (arithmetic) & greet(name) (personalized greetings)

Uses create_react_agent from LangGraph for ReAct-style reasoning

Supports real-time streaming responses

▶️ Run Instructions:

python chatbot.py


Type your queries in the terminal. Type quit to exit.

2️⃣ AI Image Classifier

A Streamlit web app that uses a pre-trained MobileNetV2 CNN model (ImageNet) to classify uploaded images.

✨ Features:

Upload .jpg, .jpeg, or .png images

Displays Top 3 predictions with confidence scores

Simple and intuitive web interface

▶️ Run Instructions:

streamlit run image_classifier.py


Open the provided local URL, upload an image, and classify it.

3️⃣ AI Resume Analyzer

A Streamlit-based AI resume analyzer powered by Gemini (Google Generative AI).

✨ Features:

Upload resumes in PDF or TXT format

Extracts and analyzes resume content automatically

Provides detailed feedback on clarity, skills, and improvements tailored to job roles

Ensures professional and constructive suggestions

▶️ Run Instructions:

streamlit run resume_analyzer.py


Upload your resume, enter a target job role, and click Analyze Resume.

⚙️ Requirements

Python 3.9+

Install dependencies:

pip install -r requirements.txt


Key Dependencies:

langchain, langchain-core, langchain-google-genai, langgraph

google-generativeai, streamlit

tensorflow, opencv-python, pillow, numpy

PyPDF2, python-dotenv

🔑 Environment Setup

Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY=your_api_key_here

📂 Folder Structure
📂 ai-mini-projects
 ├── chatbot.py            # AI chatbot with LangChain & Gemini
 ├── image_classifier.py   # Streamlit-based image classifier
 ├── resume_analyzer.py    # Resume analyzer app using Gemini
 ├── requirements.txt      # Dependencies
 └── README.md             # Project documentation

🚧 Future Improvements

Extend chatbot with additional tools (weather, knowledge retrieval, etc.)

Improve image classifier with custom-trained models

Enhance resume analyzer with job description keyword matching
