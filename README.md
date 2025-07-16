> 🇧🇷 This README is also available in [Portuguese](README.pt-BR.md).

# 🧠 Core Agent

**Core Agent** is the central brain for intelligent agents with persistent memory.
It’s designed to integrate seamlessly with interfaces (such as web chat or voice assistants), interact with multiple LLMs (like Gemini), and continuously evolve based on interactions.

> This project is the heart of your intelligent ecosystem — a foundation to build agents with memory, voice, personality, and continuous learning.

---

## ✨ Overview

Core Agent enables:

- Conversations via text or voice
- Storage of short, medium, and long-term memory
- Integration with different LLMs (Gemini, LLaMA, etc.)
- Data collection to train personalized agents
- Evolution through interactions and expert agent creation

---

## 🧠 Features

- 📚 **Persistent memory** with MongoDB
- 🧩 **Modular agent architecture ** (ex: Gemini)
- 🔁 **Collector** to train agents from interaction data
- 🧠 **Intelligent context builder**
- 🧠 **Short-term memory** (recent interactions)
- 🗣️ **TTS (Text-to-Speech)**
- 🎤 **STT (Speech-to-Text)** for voice interaction
- 💻 Functional legacy CLI interface
- 🌐 FastAPI Web-ready API (with auto documentation)

---

## ⚒️ Technologies

- **Python 3.11+**
- **FastAPI** – modern RESTful API
- **MongoDB** – memory and session database
- **Pydantic** – data validation
- **Google Generative AI** – default LLM (Gemini)
- **Docker** – local database setup
- **TTS/STT** – voice integration
- **dotenv** – environment configuration

---

## 📂 Project Structure

```
core-agent/
├── api/                # FastAPI routes
├── agents/             # Agent classes (e.g., GeminiAgent)
├── audio/              # TTS/STT support
├── cli/                # Legacy CLI (still functional)
├── core/               # Main engine (e.g., run_agent)
├── memory/             # MongoDB repository and session handling
├── scripts/            # Utility scripts (e.g., database reset)
├── utils/              # Helpers (e.g., context generation)
├── main.py             # CLI entry point
├── requirements.txt    # Project dependencies
├── docker-compose.yml  # MongoDB container setup
└── .env                # Environment variables (.env.example included)
```

---

## ⚙️ Running Locally

### Requirements

- Python 3.11+
- MongoDB running locally or via Docker

### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/core-agent.git
cd core-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate.bat  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_google_generative_ai_key
MONGO_URI=mongodb://localhost:27017
```

### 5. Run the API

```bash
uvicorn api.main:app --reload
```

Access API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run MongoDB with Docker (optional)

```bash
docker compose up -d
```

This will launch MongoDB locally on port `27017`.

---

## 🧠 About the Project

This repository is the core foundation for a planned architecture of custom intelligent applications.\

---

## 📄 License

Private for now. Considering open source release in the future.

---

## 👤 Author

Created by **Leonardo Policarpo**\
🔗 [linkedin.com/in/leonardopolicarpo](https://linkedin.com/in/leonardopolicarpo)

