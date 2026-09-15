<p align="center"><img src="branding/farmvision-logo.png" alt="FarmVision logo" width="440"></p>

<h1 align="center">🌾 FarmVision</h1>
<p align="center"><b>AI for every farmer</b> — instant crop disease diagnosis, soil-based crop & fertilizer guidance, real-location weather, and a multilingual AI assistant, all in one place.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/TensorFlow%20%7C%20PyTorch-ML-EE4C2C?logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/Groq-Llama%203.3%20Chatbot-F55036">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 🌟 Overview

FarmVision helps farmers make faster, better-informed decisions. Upload a photo of an affected leaf
and get an instant disease diagnosis, weather-aware fertilizer advice, and crop recommendations
based on real soil type — then ask follow-up questions to a multilingual AI assistant, in your own
language. Built and upgraded by **Team Vision Coders** for GDG Hackathon.

## 🧠 The problem

Farmers often lose crops to diseases that go undetected for weeks, and get generic, one-size-fits-all
advice that ignores their actual soil, location, and weather. Most agri-tech tools are also
English-only, shutting out a large share of farmers who need them most. FarmVision puts an AI
agronomist in every farmer's pocket — in their own language.

## ✨ Features

| Feature | What it does |
|---|---|
| 🍃 **Disease Detection** | Upload a leaf photo → instant AI diagnosis with a confidence score |
| 🌱 **Crop Recommendation** | Upload a soil photo → soil type classified → best-fit crops suggested |
| 🧪 **Fertilizer Advice** | Enter N-P-K values + crop → get a tailored fertilizer recommendation |
| 🌦️ **Real Location Weather** | Live weather by city search **or** your actual GPS location (browser Geolocation API) |
| 🤖 **Multilingual AI Chatbot** | Ask anything in Hindi, English, Marathi, Tamil, Telugu, Punjabi & more — powered by Groq (Llama 3.3) |
| 👨‍🌾 **Farmers Directory** | Search registered farmers on the platform |
| 📅 **Yearly Crop Planner** | Kharif / Rabi / Zaid season calendar with typical crops for each |
| 🤝 **Community Knowledge Sharing** | Farmers post and browse real tips and best practices |
| 🔐 **Accounts & Dashboard** | Signup/login (bcrypt-hashed passwords) with a personal sidebar dashboard |
| 🔥 **Firebase Logging (optional)** | Chatbot activity can optionally be logged to your own Firestore project |

## 💻 Tech stack

- **Backend:** Python, Flask, SQLAlchemy (SQLite)
- **ML / Deep Learning:** TensorFlow, Keras, PyTorch, scikit-learn, HuggingFace Transformers
- **AI Chat:** Groq API — Llama 3.3 (`groq` SDK)
- **Weather:** OpenWeatherMap API
- **Auth / Cloud (optional):** Firebase Admin SDK, Firestore
- **Frontend:** HTML, CSS (custom design system + Bootstrap), vanilla JS, browser Geolocation API

## 🛠️ Getting started

> Tested with **Python 3.11** on Windows. TensorFlow and a few ML libraries don't fully support
> Python 3.12+ yet, so 3.11 is the safe choice.

```bash
# 1. Clone and enter the project
git clone <this-repo-url>
cd FarmVision

# 2. Create and activate a virtual environment
py -3.11 -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt --default-timeout=300

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

### API keys (free, in `.env`)

| Key | Used for | Get it at |
|---|---|---|
| `OPEN_WEATHER_APIKEY` | Weather feature | https://home.openweathermap.org/users/sign_up |
| `GROQ_API_KEY` | AI chatbot | https://console.groq.com/keys |
| `HUGGINGFACE_LOGIN_TOKEN` | Optional, not required | https://huggingface.co/settings/tokens |

The app runs fine even without these — features just show a friendly setup message until the keys
are added.

### Optional: Firebase logging

Create a free project at [console.firebase.google.com](https://console.firebase.google.com), generate
a service-account key (*Project settings → Service accounts → Generate new private key*), and save it
as `firebase-credentials.json` in the project root. Skip this and the app works exactly the same.

> **First run note:** the disease-detection feature downloads a couple of HuggingFace models
> (~100–200MB) on first use — this needs internet and only happens once.

## 📂 Project structure

```
FarmVision/
├── app.py                    # Main Flask application (routes, models, ML pipeline)
├── config.py                 # Loads API keys from .env
├── requirements.txt          # Python dependencies (Python 3.11-safe)
├── .env                       # Your API keys (not committed)
├── model/                     # Trained ML models (crop, soil, disease)
├── branding/                  # Logo files (SVG + PNG)
├── utils/                     # Disease/fertilizer lookup tables + ResNet9 model class
├── templates/                 # HTML templates (dashboard, chatbot, weather, community, etc.)
├── static/css/modern.css       # Design system / visual layer
├── data/                      # Fertilizer reference data (CSV)
└── uploads/                    # Sample / user-uploaded leaf images
```

## 🗺️ Roadmap

- [ ] Farmer financial inclusion — loan eligibility check & EMI/interest calculator
- [ ] SMS-based low-tech access mode for farmers without smartphones
- [ ] Fine-tune disease models on India-specific crop data
- [ ] Migrate to PostgreSQL for production scale

## 👥 Team — Vision Coders

| Name | Role |
|---|---|
| Ujjwal Sharma | Team Lead |
| Nishant | Member |
| Aastha | Member |
| Aanya | Member |
| Nishita | Member |

## 🙏 Credits

Originally prototyped for Smart India Hackathon by Team Anant, then independently rebuilt, debugged,
rebranded, and extended by Team Vision Coders. Original research references are kept in
`README-original-SIH.md` for history.

## 🍰 Contributing

Contributions are welcome — fork, create a branch, make your changes, and open a PR.

## 🛡️ License

MIT
