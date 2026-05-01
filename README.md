# Jarvis - Voice-Activated AI Assistant

A Python-based voice assistant that listens to commands and responds intelligently using text-to-speech and AI capabilities.

## Features

- 🎤 **Voice Recognition**: Listens to and recognizes voice commands using Google Speech Recognition
- 🤖 **Voice Response**: Speaks back responses using text-to-speech synthesis
- 🧠 **AI Integration**: ChatGPT integration for intelligent responses (OpenAI API)
- 📖 **Wikipedia Integration**: Search and retrieve information from Wikipedia
- 🌐 **Web Browsing**: Open websites and search the web
- ⏰ **Time & Date**: Get current time and date information
- 🎵 **Media Control**: Play videos and music from YouTube

## Files

- **jarvis.py** - Basic Jarvis assistant with voice control and utility functions
- **jarvis_chatgpt.py** - Enhanced version with ChatGPT/OpenAI integration for intelligent responses

## Requirements

- Python 3.7+
- Microphone (for voice input)
- Speakers (for voice output)

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install SpeechRecognition pyttsx3 wikipedia pywhatkit openai
```

### Optional: ChatGPT Features

If using `jarvis_chatgpt.py`, you'll need an OpenAI API key:

1. Sign up at [OpenAI](https://openai.com)
2. Get your API key from the dashboard
3. Set the environment variable:

```bash
# Windows
set OPENAI_API_KEY=your_api_key_here

# Linux/Mac
export OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Version
```bash
python jarvis.py
```

### ChatGPT Version
```bash
python jarvis_chatgpt.py
```

The assistant will greet you and wait for voice commands. Speak clearly into your microphone.

### Example Commands

- "What time is it?"
- "Search Wikipedia for Python"
- "Open YouTube"
- "Play a video"

## Troubleshooting

- **Microphone not detected**: Check your system audio settings
- **Speech not recognized**: Speak clearly and reduce background noise
- **API errors**: Ensure your OpenAI API key is set correctly
- **pyttsx3 issues on Linux**: Install `espeak`: `sudo apt-get install espeak`

## Notes

- Voice response rate is set to 170 WPM (adjustable in code)
- Uses Google's free speech recognition API
- ChatGPT version uses gpt-4o-mini model
- Responses are limited to 200 tokens to keep them concise

## License

MIT License (or specify your preferred license)

## Author

Created as a personal voice assistant project
