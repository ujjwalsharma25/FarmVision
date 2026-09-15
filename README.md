<p align="center"><img src="branding/farmvision-logo.png" alt="FarmVision logo" width="480"></p>
<h1 align="center">🌾 FarmVision 🌾</h1>
<p align="center"><b>AI-driven crop disease detection, crop & fertilizer guidance, and a multilingual farmer assistant — for GDG Hackathon.</b></p>

## 🌟 About this project

FarmVision helps Indian farmers make faster, better-informed decisions about their crops. A farmer
uploads a photo of an affected leaf and instantly gets a disease diagnosis, weather-aware fertilizer
advice, crop recommendations based on soil type, and can now also chat in their own language with an
AI assistant for quick farming questions.

This build was upgraded for **GDG Hackathon** with a stronger focus on Google technologies and real
usability fixes (see "What's new" below).

## ✨ What's new in this build

- **🤖 Multilingual farmer chatbot** — powered by **Groq (Llama 3.3)** (free tier). Ask questions in
  Hindi, English, Marathi, Tamil, Telugu, Punjabi and more; the bot replies in the same language.
- **📍 Real GPS-based weather** — the disease-detection page now asks the browser for the farmer's
  actual location (free, built-in Geolocation API) instead of using a hardcoded fallback city, so
  fertilizer advice is based on real local weather.
- **🔥 Optional Firebase Firestore logging** — chatbot conversations can be logged to your own free
  Firebase project for analytics; the app runs perfectly fine without it too.
- **🎨 Modernized UI** — new visual layer (Google-inspired palette, modern typography) applied across
  the landing page, disease-detection flow, and the new chatbot page.
- **🐛 Fixed real deployment bugs** from the original build: hardcoded local file paths that only
  worked on the original developer's machine, a missing `config.py`, a bloated 500+ package
  `requirements.txt` that couldn't install cleanly, and a Keras/TensorFlow import mismatch.

## 🧠 Problem this solves

Farmers often lose crops to diseases that go undetected until it's too late, and struggle to get
region-specific guidance on what to plant, what fertilizer to use, and how to react to weather
patterns — rather than generic, one-size-fits-all advice. FarmVision puts an AI agronomist in every
farmer's pocket: upload a photo, get a diagnosis and a plan, in your own language.

## 🧾 Features

- Multi-crop disease detection from a leaf photo
- Fertilizer recommendation based on crop, soil, and real-time local weather
- Crop recommendation based on soil type and conditions
- Soil type classification from an image
- **Multilingual AI chatbot (Groq / Llama 3.3)** for open-ended farming questions
- Farmer accounts (signup/login) and a personal dashboard
- Optional Firebase Firestore logging of chatbot activity

## 💻 Tech stack

- **Backend:** Flask, SQLAlchemy (SQLite)
- **ML/DL:** TensorFlow/Keras, PyTorch, scikit-learn, HuggingFace Transformers
- **AI Chat:** Groq API - Llama 3.3 (`groq` SDK)
- **Auth/Cloud (optional):** Firebase Admin SDK, Firestore
- **Frontend:** HTML, CSS (custom modern layer + Bootstrap), vanilla JS (incl. browser Geolocation API)

## 🛠️ Installation & running locally

> Tested with **Python 3.11** on Windows. TensorFlow and some ML libraries don't yet fully support
> Python 3.12+, so 3.11 is the safe choice.

1. **Install Python 3.11** if you don't have it:
   https://www.python.org/downloads/release/python-3119/ (tick "Add python.exe to PATH" during install)

2. **Clone/extract this project**, then open a terminal in the project folder.

3. **Create and activate a virtual environment:**
   ```
   py -3.11 -m venv venv
   venv\Scripts\activate      # Windows
   # source venv/bin/activate   (Mac/Linux)
   ```

4. **Install dependencies:**
   ```
   pip install -r requirements.txt --default-timeout=300
   ```

5. **Set up your `.env` file** (already created, just fill in your own free keys):
   - `OPEN_WEATHER_APIKEY` — free at https://home.openweathermap.org/users/sign_up
   - `GROQ_API_KEY` — free at https://console.groq.com/keys (powers the chatbot)
   - `HUGGINGFACE_LOGIN_TOKEN` — optional, not required to run the app

6. **(Optional) Enable Firebase logging:**
   Create a free project at https://console.firebase.google.com, generate a service-account key
   (Project settings → Service accounts → Generate new private key), and save it as
   `firebase-credentials.json` in the project root. Skip this step and the app still works fine.

7. **Run the app:**
   ```
   python app.py
   ```
   Then open http://127.0.0.1:5000 in your browser.

> First run will download a couple of HuggingFace models (~100–200MB) for disease detection —
> this needs internet and only happens once.

## 📂 Project structure

```
FarmVision-main/
├── app.py                  # Main Flask application
├── config.py                # Loads weather API key from .env
├── requirements.txt          # Python dependencies (curated, Python 3.11-safe)
├── .env                     # Your API keys (not committed)
├── model/                    # Trained ML models (crop, soil, disease)
├── branding/                 # Logo files (SVG + PNG, icon + full wordmark)
├── utils/                    # Disease/fertilizer lookup + ResNet9 model class
├── templates/                # HTML templates (incl. new chatbot.html)
├── static/css/modern.css      # New modern visual layer
├── data/                    # Fertilizer reference data (CSV)
└── uploads/                  # Sample/user-uploaded leaf images
```

## 🙏 Credits

Originally built as a prototype for Smart India Hackathon 2024 by Team Anant, and since then
maintained and upgraded independently. Research references and original architecture notes are kept
in `README-original-SIH.md` for history.

## 🍰 Contributing

Open to contributions — create a branch, make your changes, and raise a PR.

## 🛡️ License

MIT.
