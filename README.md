# 🏋️ AI-GYM Trainer

An AI-powered workout assistant that uses **computer vision and pose estimation** to track exercises, count repetitions, monitor workout metrics, and provide an interactive training experience.

The project uses **MediaPipe Pose Landmarker** for real-time body-pose detection and exercise-specific logic to analyze workout movements.

## 🚀 Live Demo

👉 **Try AI-GYM Trainer:**  
https://ai-gym-coach01.streamlit.app/

---

## ✨ Features

* 🧍 **Real-time pose detection**
* 🔢 **Automatic repetition counting**
* 🏋️ **Multiple exercise support**
* 📊 **Workout metrics and tracking**
* 👤 **User authentication**
* 💾 **Workout history**
* 🤖 **AI-powered coaching**
* 🎙️ **Voice feedback**
* 🖥️ **Interactive Streamlit interface**
* 📅 **User-wise workout data tracking**

---

## 🏋️ Supported Exercises

The trainer currently supports exercises such as:

* Squats
* Bicep Curls
* Lunges
* Push-ups
* Shoulder Press

Each exercise has its own detection logic based on body landmarks and movement patterns.

---

## 🧠 How It Works

The application follows a computer-vision-based pipeline:

```text
Webcam
   ↓
Video Stream
   ↓
Pose Detection
   ↓
Body Landmarks
   ↓
Exercise Detector
   ↓
Rep / Set Tracking
   ↓
Workout Metrics
   ↓
AI / Voice Feedback
```

The camera feed is processed to detect body landmarks. These landmarks are then used by exercise-specific detectors to determine movement phases and count repetitions.

---

## 🛠️ Tech Stack

### Programming

* Python

### Computer Vision & AI

* MediaPipe
* OpenCV
* Pose Estimation
* Exercise Movement Analysis

### Application

* Streamlit
* Streamlit-WebRTC

### AI / Voice

* Groq
* gTTS

### Data

* SQLite
* Pandas

### Development

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
AI-GYM-Trainer/
│
├── core/
│   └── Video processing and core application logic
│
├── detectors/
│   ├── Biceps Curl detector
│   ├── Lunge detector
│   ├── Push-up detector
│   ├── Shoulder Press detector
│   └── Squat detector
│
├── ml_models/
│   └── Pose Landmarker model
│
├── pages/
│   └── Streamlit application pages
│
├── services/
│   ├── Authentication
│   ├── Tracking
│   ├── Metrics
│   └── Other application services
│
├── main.py
├── requirements.txt
├── packages.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-GYM-Trainer.git
cd AI-GYM-Trainer
```

### 2. Create a virtual environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the required API keys.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

> Never commit your `.env` file or API keys to GitHub.

### 5. Run the application

```bash
streamlit run main.py
```

The application will start locally and can be accessed through the Streamlit URL shown in the terminal.

---

## 🔐 Security

Sensitive files and credentials are excluded from version control using `.gitignore`.

Do not upload:

```text
.env
.venv/
*.db
API keys
personal credentials
```

---

## 🎯 Project Goals

The goal of AI-GYM Trainer is to combine:

**Computer Vision + AI + Fitness**

to create an interactive workout assistant capable of understanding exercise movements and helping users track their workouts.

---

## 🔮 Future Improvements

* 📈 Advanced workout analytics
* 🧠 Improved exercise form detection
* ⚡ More accurate repetition tracking
* 🏃 Additional exercises
* 📱 Mobile-friendly interface
* 🗣️ More advanced AI coaching
* 📊 Personalized workout recommendations
* ☁️ Cloud-based workout history
* 🏆 Progress and achievement system

---

## 👨‍💻 Author

**Raghav Pandey**

AI/ML Developer | Full Stack Developer

* GitHub: [@raghavpandey-01](https://github.com/raghavpandey-01)
* LinkedIn: [Raghav Pandey](https://www.linkedin.com/in/raghav-pandey-07bab235/)

---

## ⭐ If you like this project

If you find this project interesting, consider giving the repository a ⭐ on GitHub.
