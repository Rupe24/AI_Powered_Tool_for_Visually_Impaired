# 👁️‍🗨️ AI-Powered Assistive Tool for Visually Impaired

---

## 📌 About the Project

This AI-powered assistive tool is designed to help visually impaired individuals interact with their environment using artificial intelligence. It combines real-time object detection, text reading with audio output, and smart navigation features in a single, unified platform with a simple Streamlit-based user interface.

### 🔍 Object Detection
- Uses **YOLOv8** to identify and recognize surrounding objects from the camera feed.

### 📝 Text Recognition & Audio Output
- Uses **EasyOCR** to extract text from images.
- Converts recognized text to audio using **pyttsx3**, enabling offline voice feedback.

### 🧭 Navigation Support
- Utilizes **OpenRouteService API (ORS)** to provide walking directions based on source and destination inputs.

---

## 💻 User Interface

- Built with **Streamlit**, offering a clean and accessible interface.
- Provides easy access to:
  - Object Detection
  - Text Reader
  - Navigation Module
  - Gemini AI Assistant (optional) for interactive communication

---

## 🧠 Voice Activation & Intents

- The system is designed to be **invoked using a wake word**.
- After activation, users must provide specific **intents** to trigger the correct module:
  - For object detection → say something like **"Detect objects"**
  - For text reading → say **"Read this"**
  - For navigation → say **"Guide me to [destination]"**
  - For AI Assistant → say **"Talk to assistant"** or similar

This voice-command structure improves accessibility for visually impaired users by reducing the need for manual control.

---

## 🧠 Technologies Used

| Module              | Technology Used               |
|---------------------|-------------------------------|
| Object Detection    | YOLOv8 (Ultralytics)          |
| Text Recognition    | EasyOCR                       |
| Image Processing    | OpenCV                        |
| Text-to-Speech      | pyttsx3                       |
| Navigation          | OpenRouteService API (ORS)    |
| User Interface      | Streamlit                     |
| Optional Assistant  | Gemini AI                     |

---

## ⚠️ Note

> The full code is **not** provided in this repository.  
> If you need the complete source code, contact **roopeshrupe1524@gmail.com**
