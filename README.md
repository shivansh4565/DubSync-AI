# 🎬 DubSync AI

> **AI-Powered Multilingual Video Dubbing Platform**

DubSync AI is an AI-powered video dubbing platform that automatically transcribes speech from a video, identifies different speakers, translates the dialogue into a target language, generates AI speech, and merges the translated audio back into the original video while preserving the conversation flow.

---

## 🚀 Features

- 📤 Upload video files
- 🎙️ Automatic speech-to-text using Faster Whisper
- 👥 Multi-speaker segmentation
- 🌍 Translate speech into another language
- 🔊 AI voice generation using Google Text-to-Speech
- 🎥 Merge translated audio with original video
- 📥 Download the final dubbed video
- ⚡ FastAPI REST API
- 🐳 Docker support

---

## 🏗️ Architecture

```
                Upload Video
                      │
                      ▼
            Audio Extraction (FFmpeg)
                      │
                      ▼
          Speech-to-Text (Faster Whisper)
                      │
                      ▼
          Speaker Segmentation
                      │
                      ▼
           Language Translation
                      │
                      ▼
         Text-to-Speech Generation
                      │
                      ▼
         Audio & Video Merging
                      │
                      ▼
          Download Dubbed Video
```

---

# 📁 Project Structure

```
DubSync-AI/
│
├── app/
│   ├── api/
│   │   ├── upload.py
│   │   ├── process.py
│   │   ├── status.py
│   │   └── download.py
│   │
│   ├── core/
│   │   ├── extractor.py
│   │   ├── transcriber.py
│   │   ├── diarization.py
│   │   ├── translator.py
│   │   ├── tts.py
│   │   ├── video_merger.py
│   │   └── pipeline.py
│   │
│   ├── models/
│   └── services/
│
├── uploads/
├── outputs/
├── temp/
├── tts_output/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
└── README.md
```

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- Python 3.11

### AI/ML

- Faster Whisper
- Google Text-to-Speech (gTTS)
- Deep Translator

### Media Processing

- FFmpeg
- Pydub

### Deployment

- Docker
- Docker Compose

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/DubSync-AI.git

cd DubSync-AI
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 🐳 Docker

## Build

```bash
docker build -t dubsync-ai .
```

## Run

```bash
docker run -p 8000:8000 dubsync-ai
```

or

```bash
docker compose up --build
```

---

# 📌 API Endpoints

## Upload Video

```
POST /upload
```

Uploads a video and returns a Job ID.

---

## Process Video

```
POST /process/{job_id}
```

Starts the dubbing pipeline.

---

## Check Status

```
GET /status/{job_id}
```

Returns the current processing status.

---

## Download Output

```
GET /download/{job_id}
```

Downloads the final dubbed video.

---

# 🔄 Processing Pipeline

```
Video Upload
      │
      ▼
Audio Extraction
      │
      ▼
Speech Recognition
      │
      ▼
Speaker Detection
      │
      ▼
Translation
      │
      ▼
Text-to-Speech
      │
      ▼
Video Rendering
      │
      ▼
Download
```

---

# 📷 Demo

## Upload Video

> Upload any supported video file through the web interface.

---

## Processing

The application automatically:

- Extracts audio
- Transcribes speech
- Detects speakers
- Translates dialogue
- Generates dubbed speech
- Produces the final dubbed video

---

## Output

Download the translated and dubbed video directly from the application.

---

# 🌟 Future Improvements

- Real-time dubbing
- Better speaker diarization using PyAnnote
- Voice cloning
- Lip synchronization
- Multiple target languages
- GPU acceleration
- Cloud storage support

---

# 📄 License

This project is developed for educational and assignment purposes.

---

# 👨‍💻 Author

**Shivansh Saxena**

- GitHub: https://github.com/shivansh4565
- LinkedIn: https://www.linkedin.com/in/shivansh-saxena

---

## ⭐ If you found this project useful, consider giving it a star!
