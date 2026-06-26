# 🧠 Mental Health AI Chatbot | Generative AI with Gemini

> **An AI-powered conversational assistant built using Google's Gemini Large Language Model (LLM) to provide empathetic, context-aware mental health support through responsible AI practices and prompt engineering.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![LLM](https://img.shields.io/badge/LLM-Generative%20AI-success)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-orange)

---

## 📖 Project Overview

Mental health support should be accessible, empathetic, and available whenever users need it. Advances in Large Language Models (LLMs) enable conversational AI systems that can provide supportive interactions while following responsible AI principles.

This project implements a **Mental Health AI Chatbot** powered by **Google Gemini**, capable of generating empathetic, context-aware responses while maintaining safety guardrails and encouraging professional help when appropriate.

The chatbot demonstrates practical applications of **Generative AI, Prompt Engineering, Large Language Models, and conversational AI development**.

> **Disclaimer:** This chatbot is intended for educational purposes and general emotional support only. It is **not** a substitute for professional medical, psychological, or emergency care.

---

## 🎯 Project Objectives

* Build an AI-powered conversational assistant
* Generate empathetic and context-aware responses
* Implement responsible AI safety guardrails
* Maintain multi-turn conversation memory
* Deploy an interactive chatbot using Streamlit
* Gain hands-on experience with Generative AI application development

---

## ✨ Key Features

### Intelligent Conversations

* Natural language interaction
* Context-aware AI responses
* Multi-turn conversation support

### Prompt Engineering

* Structured system prompts
* Empathetic response generation
* Controlled response behavior
* Safety-focused instructions

### Responsible AI

* Avoids harmful or judgmental responses
* Does not provide medical diagnoses
* Encourages professional support when appropriate
* Includes safety disclaimers

### Streamlit Interface

* Interactive chat interface
* Real-time responses
* Session-based conversation history
* Clean and responsive UI

### Gemini Integration

* Google Gemini API
* Fast LLM inference
* Environment-based API key management

---

## 🏗️ System Architecture

```text
User Message
      │
      ▼
Streamlit Interface
      │
      ▼
Conversation Memory
      │
      ▼
Prompt Engineering Layer
      │
      ▼
Google Gemini API
      │
      ▼
Response Validation
      │
      ▼
AI Response
```

---

## 🛠️ Technology Stack

| Category        | Technologies             |
| --------------- | ------------------------ |
| Programming     | Python                   |
| Frontend        | Streamlit                |
| LLM             | Google Gemini            |
| AI              | Google Generative AI SDK |
| Configuration   | python-dotenv            |
| Data Processing | Pandas                   |

---

## 📂 Project Structure

```text
mental_health_genai_chatbot/
│
├── app/
│   ├── api/
│   │   └── gemini_client.py
│   │
│   ├── prompts/
│   │   └── system_prompt.py
│   │
│   ├── memory/
│   │   └── session_memory.py
│   │
│   ├── services/
│   │   └── chatbot_service.py
│   │
│   └── utils/
│       └── logger.py
│
├── config.py
├── main.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/pranjalsalvi/mental-health-genai-chatbot.git

cd mental-health-genai-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Run the Application

```bash
streamlit run main.py
```

Open your browser and begin interacting with the chatbot.

---

## 🔍 Application Workflow

1. User submits a message.
2. Conversation history is retrieved.
3. A structured system prompt is applied.
4. User input is sent to the Gemini model.
5. Gemini generates an empathetic response.
6. The response is displayed while maintaining conversation context.

---

## 💡 Key Highlights

* Google Gemini LLM Integration
* Prompt Engineering
* Context-Aware Conversations
* Responsible AI Principles
* Session-Based Memory
* Modular Python Architecture
* Streamlit Deployment

---

## 📌 Applications

The architecture can be adapted for:

* Mental Health Assistants
* Healthcare Chatbots
* Educational AI Tutors
* HR Helpdesks
* Customer Support Systems
* Internal Knowledge Assistants
* Wellness Applications

---

## 🚀 Future Enhancements

* Long-term conversation memory using MongoDB or PostgreSQL
* Emotion detection through sentiment analysis
* Voice-based interaction
* Multi-language support
* Crisis detection with emergency resource recommendations
* User authentication
* Cloud deployment (AWS, Azure, GCP, or Render)
* Analytics dashboard for conversation insights

---

## 👨‍💻 About Me

**Pranjal Salvi**

Aspiring **Data Analyst & AI Engineer** passionate about Generative AI, Large Language Models (LLMs), Machine Learning, NLP, and building intelligent applications.

### Connect with me

* 🔗 LinkedIn: https://www.linkedin.com/in/pranjal-salvi-380732227/
* 💻 GitHub: https://github.com/pranjalsalvi

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

Your support motivates me to continue building AI-powered applications and sharing open-source projects.

---

### Thank you for visiting this repository! 🚀
