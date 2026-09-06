# RAG AI Barista ☕

An AI-powered coffee shop assistant built with **Google ADK, Gemini, Streamlit, and Python**.

## Overview

RAG AI Barista is a Retrieval-Augmented Generation (RAG) application that helps customers choose drinks and pastries based on their preferences.

The AI agent retrieves information from a coffee shop menu and uses Gemini to provide grounded recommendations.

The agent is designed to recommend **only items available in the menu** and consider tags, descriptions, and allergens when making recommendations.

## Features

- 🤖 AI-powered coffee shop assistant
- 🔎 Menu-based information retrieval
- ☕ Drink and pastry recommendations
- 🥛 Allergen-aware recommendations
- 💬 Interactive Streamlit chat interface
- 🧠 Google Agent Development Kit (ADK)
- 🔐 Secure Gemini API key handling using environment variables

## Technologies

- Python
- Google Agent Development Kit (ADK)
- Gemini API
- Streamlit
- JSON
- Git & GitHub

## Project Structure

```text
rag-ai-barista/
├── app.py
├── agent.py
├── tools.py
├── menu.json
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── .env
