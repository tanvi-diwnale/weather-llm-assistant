# 🌦 Weather Assistant – LLM Powered Application

A full-stack web application that allows users to ask natural-language weather queries (e.g., *“What is the weather in Pune?”*) and receive real-time responses using a Large Language Model integrated with a weather tool.

---

## 📌 Project Overview

This project demonstrates the integration of a **React frontend** with a **FastAPI backend**, where user queries are processed using **LangChain** and an **LLM via OpenRouter**.  
The backend intelligently detects weather-related queries and fetches live weather data using the **OpenWeatherMap API**, returning a human-readable response.

---

## 🛠 Tech Stack

### Frontend
- React
- JavaScript
- HTML & CSS

### Backend
- FastAPI
- Python
- LangChain
- OpenRouter (LLM provider)

### External APIs
- OpenWeatherMap API

---

## 🔄 Application Workflow

1. User enters a weather-related query in the frontend.
2. React sends the query to the FastAPI backend.
3. LangChain agent analyzes the intent of the query.
4. Weather tool fetches live weather data for the detected city.
5. LLM generates a natural-language response.
6. Response is displayed on the frontend UI.

---

## ✨ Features

- Natural language weather queries
- LLM + tool-based backend architecture
- Clean and responsive UI
- Modular and scalable project structure
- Secure handling of API keys using environment variables

---

## 📁 Project Structure

weather-llm-app/
│
├── backend/
│ ├── app/
│ │ ├── agent.py
│ │ ├── main.py
│ │ ├── config.py
│ │ └── tools/
│ │ └── weather_tool.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/
│ ├── public/
│ └── src/
│ ├── components/
│ ├── services/
│ └── App.js
│
└── README.md