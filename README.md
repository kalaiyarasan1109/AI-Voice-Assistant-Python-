# AI Voice Assistant (Python)

A real-time AI-powered **Windows voice assistant** built using **Python**, **Google Gemini Realtime API**, and **LiveKit**.
The assistant listens to voice commands, responds intelligently, and performs desktop actions like opening applications.

---

## 🚀 Features

* 🎙️ **Real-time voice interaction**
* 🤖 Powered by **Google Gemini Realtime API**
* 🖥️ Opens Windows applications via voice commands:

  * Notepad
  * Calculator
  * Microsoft Word
  * Microsoft Excel
* 😴 **Sleep & wake functionality**
* 🔇 Built-in **noise cancellation** using LiveKit
* 🔐 Secure environment variable handling with `.env`

---

## 🛠️ Tech Stack

* **Python**
* **LiveKit Agents SDK**
* **Google Gemini Realtime API**
* **Asyncio**
* **dotenv**
* **Windows subprocess automation**

---

## 📂 Project Structure

```
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the Application

```bash
python main.py
```

The assistant connects to a LiveKit room and starts listening for voice input.

---

## 🗣️ Example Voice Commands

* **“Open Notepad”**
* **“Open Calculator”**
* **“Open Excel”**
* **“Go to sleep”**
* **“Nova”** (wake up)
* **“Exit” / “Shutdown”**

---

## 🧠 How It Works (High Level)

1. Captures live audio input using **LiveKit**
2. Processes speech with **Google Gemini Realtime**
3. Uses **function tools** to map voice intent to system actions
4. Executes desktop commands using Python subprocess
5. Responds back with real-time voice output

---

## 🔐 Security Notes

* API keys are stored securely using environment variables
* No hardcoded credentials
* Designed for local execution only

---

## 🎯 Use Cases

* Voice-controlled desktop automation
* Real-time AI assistant prototypes
* Learning project for:

  * AI agents
  * Realtime APIs
  * Voice interfaces
  * Async Python

---

## 📌 Skills Demonstrated

* AI agent design
* Real-time voice systems
* API integration
* Async programming
* Desktop automation
* Clean, modular Python code
