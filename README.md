# AI Text Assistant

A command-line AI assistant built with Python, LangChain, and Google's Gemini API.

The project was developed as part of my AI learning journey, with the goal of understanding how modern LLM applications are structured and how conversation-based AI systems work.

## Features

- Interactive command-line chat
- Conversation history
- Sliding-window conversation memory
- Configurable AI model and conversation length
- User-friendly API error handling
- Secure API key management using environment variables
- LangChain LCEL pipeline

## Technologies

- Python
- LangChain
- Google Gemini API
- python-dotenv
- Git & GitHub

## How It Works

The application follows a simple LangChain pipeline:

```text
User Input
    ↓
Conversation History
    ↓
Chat Prompt Template
    ↓
Gemini Model
    ↓
StrOutputParser
    ↓
AI Response
    ↓
Conversation History