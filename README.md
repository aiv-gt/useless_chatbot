<p align="center">
  <img src="useless-chatbot/frontend/logo.jpg" alt="Useless Chatbot Logo" width="180" />
</p>

<h1 align="center">Useless Chatbot 💀</h1>

<p align="center">
  A chatbot that takes your messages seriously... just kidding.
</p>

Instead of trying to be helpful, the Useless Chatbot is designed to give pointless, sarcastic, random, and sometimes emotionally inappropriate responses. Depending on what you say, it can respond with text, a different emotion, or a reaction meme.

## Basic Details

### Team Name: HMM

### Team Members
- **Abhinav Ajayakumar** - Sree Buddha College of Engineering, Pattoor
- **Thejas A** - Sree Buddha College of Engineering, Pattoor

### Project Description

Useless Chatbot is a deliberately unhelpful conversational application created for the TinkerHub Useless Projects initiative. It detects simple categories in a user's message and responds using scripted replies with intentionally weird emotions, sarcasm, or meme reactions.

The project combines a browser-based chat interface with a Python FastAPI backend and a collection of locally stored reaction memes.

### The Problem (that doesn't exist)

People keep asking chatbots for useful answers.

What if, instead of solving problems, a chatbot made the conversation even more confusing?

### The Solution (that nobody asked for)

We built a chatbot that refuses to take conversations seriously.

It recognizes categories such as greetings, bragging, success, failure, sadness, anger, boredom, love, insults, thanks, apologies, and questions. It then selects a deliberately useless response or sends a reaction meme. Questions are specially handled with a sarcastic meme response.

The system also supports Malayalam/Manglish-style phrases in several categories to make the responses feel more natural to our target users.

## Technical Details

### Technologies/Components Used

#### Software
- Python
- FastAPI
- Uvicorn
- Pydantic
- HTML5
- CSS3
- JavaScript
- Regular expressions (`re`)
- Local JPG reaction memes

### Architecture

```text
User
  ↓
Web Frontend (HTML + CSS + JavaScript)
  ↓
POST /api/chat
  ↓
FastAPI Backend
  ↓
Message Normalization
  ↓
Category Detection using Regex Patterns
  ↓
Scripted Response Selection
  ↓
Text / Emotion / Meme
  ↓
Frontend displays the reaction
```

### How It Works

1. The user enters a message in the web interface.
2. JavaScript sends the message to the FastAPI `/api/chat` endpoint.
3. The backend normalizes the text and detects a category using editable regular-expression patterns.
4. A response is selected from the corresponding scripted reply collection.
5. The backend returns `text`, `emotion`, and optionally a meme path.
6. The frontend displays the text response or meme reaction.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aiv-gt/hmm.git
cd hmm/useless-chatbot/backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run

### 1. Start the backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 2. Open the frontend

Open:

```text
useless-chatbot/frontend/index.html
```

The frontend is configured to send requests to the local FastAPI server at `http://127.0.0.1:8000`.

## Features

- Intentionally useless responses
- Category-based message detection
- Different emotional reactions
- Local reaction memes
- 🇮🇳 Malayalam/Manglish-style phrase support
- Special handling for questions
- New Chat option
- Browser-based frontend
- FastAPI backend API
- Easy-to-edit response and category files

## Project Structure

```text
hmm/
├── README.md
└── useless-chatbot/
    ├── backend/
    │   ├── main.py
    │   ├── replies.py
    │   ├── response_engine.py
    │   └── requirements.txt
    │
    └── frontend/
        ├── index.html
        ├── logo.jpg
        ├── css/
        │   └── style.css
        ├── js/
        │   └── app.js
        └── memes/
            └── *.jpg
```

## Screenshots

### Landing Page

![Chatbot Response](screenshots/landing-page.jpg)

### Main Chat Interface

![Main Chat Interface](screenshots/chat-interface.jpg)

### Chatbot Conversation

![Chatbot Conversation](screenshots/chat-conversation.jpg)

## Team Contributions

- **Abhinav Ajayakumar:** Project development, backend logic, category detection, response engine, API integration, and project integration.
- **Thejas A:** Frontend/UI development, interaction design, testing, and project integration.

## Future Improvements

- Add more response categories and meme reactions.
- Add persistent chat history.
- Add more expressive frontend animations.
- Improve message classification beyond keyword/regex matching.
- Add deployment support so the chatbot can be accessed online.

---

Made with ❤️ at TinkerHub Useless Projects

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)
