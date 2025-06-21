# 🎙️ Responsive Text-to-Speech (TTS) App

## 🌐 Overview
A full-stack responsive Text-to-Speech (TTS) web app that converts user input into natural-sounding speech using an open-source model.  
Supports **Hindi** and **English**, with audio served as a streaming response via a Python FastAPI backend.

---

## ▶️ Preview


https://github.com/user-attachments/assets/a63b314d-14a2-4a41-ba27-095e44634a26

---

## ⚙️ Setup Instructions

### 🔧 Clone & Install

```bash
git clone https://github.com/YA-shiKa/text2speech
cd text2speech
python3.10 -m venv venv310  # Ensure Python 3.10.13 is installed
venv310\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
uvicorn app:app --reload
```
Then open your browser and go to:
```bash
http://127.0.0.1:8000
```

---

## 🎤 API Usage
✅ POST /speak

- Request: multipart/form-data

```bash
{
  "text": "Namaste, how are you?"
}
  ```
- Response:
audio/mpeg streaming audio

---

## ✨ Integration with OpenAI SDK
You can use OpenAI’s tts_to_file() method with this server:

```bash
from openai import OpenAI

openai.tts_to_file(
    text="Hello world",
    file_path="output.mp3",
    voice="http://127.0.0.1:8000/speak"
)
 ```

 ---

## 🌟 Features

- ✅ Open-source TTS model (`vits` via Coqui TTS)  
- 🗣️ Hindi + English support  
- 📡 Real-time audio streaming (FastAPI)  
- 💻 Responsive Web UI (HTML + JavaScript)  
- 🧪 Compatible with OpenAI’s `tts_to_file()` API

---

## 📦 Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Coqui TTS
- Pydub
- FFmpeg (must be installed & added to PATH)
- SoundFile
- Langdetect



