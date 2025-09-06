# Cyrus - Build smarter workflows with Cyrus – Adapt it. Expand it. Own it.

# Introduction
Cyrus AI is a live server-based AI assistant built using Python. & also 
It allows users to interact with an intelligent AI in real-time for answering questions, automating tasks, and providing recommendations. 
The system is hosted using LiveKit server, enabling smooth, real-time interactions.

### ✨ Features
- **Voice-activated interactions** — Ask Cyrus to send WhatsApp messages, fetch live directions, set timers, or more—completely hands-free.
- **LiveKit-powered** — Real-time voice communication, with background noise cancellation and responsive agent behavior.
- **Tool integrations**:
  - WhatsApp automation via browser pre-fill
  - Live Google Maps directions from current location
  - Timer setup with voice triggers
  - And more features in pipeline (news, jokes, reminders…) & it also works on
# Real-time Interaction: Converse with the AI instantly through LiveKit server.
# Task Automation: Perform simple calculations, reminders, or file-related tasks.
# Knowledge Assistance: Get answers to questions or explanations of concepts.
# Customizable Modules: Easily add new functionality to enhance the AI assistant.
# Cross-platform Usage: Works on any device that can run Python and connect to the server.

###  LiveKit Flow
Cyrus runs as a LiveKit agent:
1. User speaks via mic.
2. Agent uses speech-to-text to understand commands by using the livekit plugins.
3. Commands like messaging or map queries get executed via web browser.
4. Agent responds back via voice or log.

###  Setup & Installation
####  Prerequisites
- Python 3.11 (recommended; required for PyAudio compatibility)
- A working microphone
- Gmail App Password (for email feature if implemented)

# File Structure
├── cyrus.py              # This is the model provided by livekit server in the website
├── logic.py              # In this file i have implemented the real time working of code
├── instruction.txt      # In this i have given the instruction how to introduce and how to get intreact with the user 
├── README.md             # This
└── venv/                 # (optional) Virtual environment folder this file conatins the API keys
