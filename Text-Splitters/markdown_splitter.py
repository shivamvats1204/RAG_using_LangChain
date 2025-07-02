from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text="""
# Sage: Advanced AI Chatbot Assistant

## Overview

**Sage** is an advanced AI-powered desktop assistant featuring a modern graphical user interface (GUI), real-time search, conversational AI, automation, speech-to-text, text-to-speech, and image generation capabilities. It is designed to help users interact naturally with their computer, automate tasks, retrieve up-to-date information, and generate content or images using state-of-the-art AI models.

---

## Features

- **Conversational AI**: Chat with Sage using natural language. Sage can answer questions, provide explanations, and maintain context.
- **Real-Time Search**: Fetches up-to-date information from the web using Google and YouTube search.
- **Automation**: Open/close applications, play YouTube videos, control system volume, and more.
- **Content Generation**: Write letters, emails, code, essays, and more using AI.
- **Image Generation**: Generate high-quality images from text prompts using Stable Diffusion.
- **Speech-to-Text**: Speak to Sage and have your speech transcribed and processed.
- **Text-to-Speech**: Sage can read out responses using realistic AI voices.
- **Modern GUI**: Built with PyQt5, featuring chat history, status indicators, and animated graphics.

---
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=500,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(len(chunks))  # Print the number of chunks created
print(chunks)  # Print the first chunk