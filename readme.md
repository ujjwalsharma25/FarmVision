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


## 📚📚 Research And References: (Some Proven Theories' which validates this POC)

1.Development of Machine Learning Methods for Accurate Prediction of Plant Disease Resistance (2024): https://www.sciencedirect.com/science/article/pii/S2095809924002431

2.Chinese cabbage leaf disease prediction and classification using Naive Bayes VGG-19 convolution deep neural network (2024) : https://ieeexplore.ieee.org/document/10407076

3.Image-based crop disease detection with federated learning (2023): https://www.nature.com/articles/ s41598-023-46218-5

3.Deep learning-based crop disease prediction with web application (2023) : https://www. sciencedirect.com/science/article/pii/S2666154323002715

4.Seasonal Crops Disease Prediction and Classification Using Deep Convolutional Encoder Network (2019): https://link.springer.com/article/10.1007/s00034-019-01041-0 Cropin app link: https://www.cropin.com/farming- apps#:~:text=Cropin%20Grow%20is%20a%20robust, stakeholders%20in%20the%20agri%2Decosystem.


## ✅❇️ Problem ArogyaKrishi Addresses and Solves :

Arogya Krishi is an agricultural application that addresses critical challenges faced by farmers, including crop disease detection, optimal crop recommendations, and soil health assessment. It provides tailored fertilizer suggestions and integrates real-time weather data to help farmers make informed decisions. With a user-friendly interface and community engagement features, Arogya Krishi empowers farmers to enhance productivity and sustainability in their agricultural practices.

Arogya Krishi: Problem Descriptions and Solutions
Arogya Krishi is a comprehensive agricultural application designed to address various challenges faced by farmers and agricultural stakeholders. Below are the key problems it addresses and the solutions it provides:

1. Crop Disease Detection:

Problem: Farmers often struggle to identify diseases affecting their crops, leading to reduced yields and economic losses. Early detection is crucial for effective management and treatment.

Solution: Arogya Krishi utilizes advanced image classification techniques powered by machine learning to analyze images of crops. The application can accurately identify diseases and provide detailed information about the disease, enabling farmers to take timely action.

2. Crop Recommendation:

Problem: Farmers may lack knowledge about which crops are best suited for their specific soil types and climatic conditions, leading to poor crop choices and low productivity. Solution: The application offers crop recommendation features based on soil analysis and environmental factors. By analyzing soil characteristics and local climate data, Arogya Krishi suggests optimal crops that can thrive in the given conditions, enhancing productivity and profitability.

3. Fertilizer Recommendations:

Problem: Farmers often face challenges in determining the right type and amount of fertilizers to use, which can lead to overuse or underuse, affecting crop health and the environment. Solution: The application generates tailored fertilizer recommendations based on the specific crop being cultivated, soil health, and environmental conditions. This helps farmers optimize their fertilizer usage, improving crop yields while minimizing environmental impact.

4. Weather Data Integration:

Problem: Farmers need access to real-time weather data to make informed decisions about planting, irrigation, and harvesting. Lack of timely weather information can lead to crop losses. Solution: Arogya Krishi integrates weather data from reliable sources, providing farmers with current weather conditions, forecasts, and alerts. This information helps farmers plan their activities more effectively, reducing risks associated with adverse weather.

6. User-Friendly Interface:

Problem: Many agricultural technologies are complex and difficult for farmers to use, especially those with limited technical knowledge. Solution: Arogya Krishi is designed with a user-friendly interface that simplifies navigation and usage. It provides clear instructions and visual aids, making it accessible to farmers of all backgrounds.

7. Community and Knowledge Sharing:

Problem: Farmers often work in isolation and may lack access to shared knowledge and experiences from their peers. Solution: The application can facilitate community engagement by allowing users to share their experiences, tips, and best practices. This fosters a sense of community and encourages collaborative learning among farmers.


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


## 📈 Feasibility Analysis:

• High Feasibility: Advanced ML models and cloud deployment enable real-time disease prediction.

• Scalability: Supports multilingual features

• Personalized Alerts: Farmers get alerts based on crop type, region, and disease severity.


## ⚓ Potential Challenges & Risks:

• Data Quality: Poor data leads to inaccurate predictions

• Accuracy of AI Models: Risk of false positives and false negatives cases.

• Environmental Variability: Presence of Diverse conditions. Viability Analysis:

• Early Detection: Detects diseases early, lowering treatment costs and preventing spread.


## 🪄🔮 Impact And Benifities:

• Economic Benefits: Lowers disease management costs, increasing productivity.

• Environmental Impact: Optimizes pesticide/fertilizer use, promoting sustainability.

• Data-Driven Decisions: Provides real-time insights for efficient farm management.

• Resilience: Enhances farming practices and reduces risks of disease outbreaks.

• Uniqueness:

1.Identify crop diseases

2.Predict disease outbreaks

3.Recommend preventive measure

4.Optimize resource allocation

5.Enhance agricultural productivity

6.Real-time performance

7.Userfriendliness

8.Scalability


## 🗺️ Future Roadmap

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



## 🛡️ License

MIT
