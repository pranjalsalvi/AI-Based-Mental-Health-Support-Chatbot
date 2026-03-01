# 🧠 Mental Health GenAI Chatbot  

---

## 📌 Project Overview  

This project focuses on building a **Mental Health Generative AI Chatbot** using modern **Natural Language Processing (NLP)** and **Large Language Model (LLM)** capabilities.  

The chatbot is designed to provide **empathetic, supportive, and safe responses** to users seeking mental health guidance.  

The objective is to create an interactive AI assistant that can:  

- Offer emotional support  
- Provide general coping strategies  
- Encourage professional help when necessary  
- Maintain safe and responsible AI behavior  

This project emphasizes **Natural Language Processing, Generative AI, prompt engineering, and real-time chatbot deployment**, without complex production-level MLOps pipelines.  

---

## 🎯 Objectives  

- Build an AI-powered conversational chatbot for mental health support  
- Generate empathetic and context-aware responses  
- Ensure safe AI responses using responsible AI guidelines  
- Deploy the chatbot using a simple web interface  
- Gain hands-on experience with Generative AI and LLM integration  

---

## 🧠 Technologies Used  

### 👨‍💻 Programming & Libraries  

- **Python**  
- **Streamlit**  
- **Google Generative AI (Gemini API)**  
- **Pandas** 
- **dotenv** (for API key management)  

### 🤖 AI Model  

- **Google Gemini (Generative AI model)**
---

## 📂 Project Structure  
```
mental_health_genai_chatbot/
│
├── app/                         # Main application package
│   ├── __init__.py
│   │
│   ├── api/
│   │   └── gemini_client.py     # Gemini API integration
│   │
│   ├── prompts/
│   │   └── system_prompt.py     # Prompt engineering module
│   │
│   ├── memory/
│   │   └── session_memory.py    # Multi-turn conversation memory
│   │
│   ├── services/
│   │   └── chatbot_service.py   # Core chatbot logic
│   │
│   └── utils/
│       └── logger.py            # Logging configuration
│
├── config.py                    # Environment configuration
├── main.py                      # Streamlit UI entry point
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🔍 Project Description  

### 🗣️ What the Chatbot Does  

The **Mental Health Chatbot**:  

- Accepts user input (feelings, stress, anxiety-related messages)  
- Uses a Generative AI model to generate supportive responses  
- Provides coping strategies (breathing, journaling, mindfulness tips)  
- Encourages seeking professional help in severe cases  
- Avoids harmful, judgmental, or medical-diagnosis responses  

⚠️ **Disclaimer:**  
This chatbot is not a replacement for professional medical or psychological treatment. It provides general guidance and emotional support only.  

---

## ⚙️ Project Workflow  

### 1. Environment Setup  

- Create virtual environment  
- Install required libraries  
- Configure API key using `.env`  

---

### 2. Prompt Engineering  

- Design a structured prompt template  
- Include empathy instructions  
- Restrict harmful or unsafe responses  
- Add safety disclaimers when needed  

---

### 3. Model Integration  

- Connect to Google Gemini API  
- Pass user input to the model  
- Receive and display generated response  

---

### 4. Streamlit Deployment  

- Create chat interface using Streamlit  
- Maintain session state for chat history  
- Display conversation in real-time  

Run the app using:  
```
streamlit run main.py
```


---

## 📊 Features Implemented  

- ✅ Real-time conversational interface  
- ✅ Context-aware AI responses  
- ✅ Clean and simple UI  
- ✅ Session-based chat memory  
- ✅ Basic safety guardrails  
- ✅ API-based LLM integration  

---

## 📈 Results & Insights  

- The chatbot generates empathetic and supportive responses  
- Prompt design significantly impacts response quality  
- Guardrails help prevent unsafe or harmful outputs  
- Real-time AI applications can be built efficiently using Streamlit  

---

## 🏁 Conclusion  

This project demonstrates how **Generative AI and Large Language Models** can be used to create meaningful and supportive conversational applications.  

It provides practical experience in:  

- Prompt engineering  
- API integration  
- AI safety practices  
- Real-time chatbot deployment  

---

## 🚀 Future Enhancements  

- Add conversation memory using database (MongoDB / MySQL)  
- Implement emotion detection using sentiment analysis  
- Add multi-language support  
- Deploy on cloud (AWS / Render / GCP)  
- Integrate crisis detection with emergency helpline suggestions  
- Improve UI/UX with advanced chat styling  

---

## 👤 Author  

**Pranjal Salvi**  
Data Science Student  

---

## ⭐ Acknowledgements  

- Google Generative AI (Gemini API)  
- Streamlit  
- Open-source AI & Data Science community  
