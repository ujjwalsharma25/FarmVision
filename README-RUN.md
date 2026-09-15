# FarmVision — Quick Setup Guide (Windows)

Detailed English docs: `README.md`. Ye Hinglish quick-reference hai.

## Is version mein kya naya/fix hai:
- Hardcoded `D:\...` paths hata ke relative paths kiye (app.py)
- Missing `config.py` bana di
- ML models `model/` folder mein sahi naam se daale
- `requirements.txt` clean kiya (Python 3.11-safe versions)
- `tensorflow.keras` → `keras` import fix (crash fix)
- Debug-mode auto-restart crash fix (`use_reloader=False`)
- **Real GPS location bug fix** — pehle hamesha Mumbai ka weather use hota tha chahe farmer kahin bhi ho; ab browser se real location leta hai
- **Naya: Groq multilingual chatbot** (`/chatbot`) — free Groq API key se
- **Naya: Firebase Firestore logging** (optional, free)
- **UI modernize** kiya — naya `static/css/modern.css`

## Step 1 — Python 3.11 install karo (agar nahi hai)
https://www.python.org/downloads/release/python-3119/ — install karte waqt "Add python.exe to PATH" tick karna.

## Step 2 — Zip extract karke VS Code mein kholo, terminal kholo (Ctrl + `)

## Step 3 — Virtual environment banao
```
py -3.11 -m venv venv
venv\Scripts\activate
```

## Step 4 — Dependencies install karo
```
pip install -r requirements.txt --default-timeout=300
```
5-10 min lag sakta hai (TensorFlow/PyTorch bhaari hain), net stable rakhna.

## Step 5 — `.env` file mein apni free API keys daalo
File already bani hui hai, bas values bhar do:
- `OPEN_WEATHER_APIKEY` — https://home.openweathermap.org/users/sign_up (2 min)
- `GROQ_API_KEY` — https://console.groq.com/keys (console pe sign in karo, 1 min) — ye chatbot ke liye chahiye
- `HUGGINGFACE_LOGIN_TOKEN` — optional, chhod bhi sakte ho

## Step 6 (Optional) — Firebase activate karna ho to
1. https://console.firebase.google.com pe free project banao
2. Project settings → Service accounts → "Generate new private key"
3. Downloaded JSON file ko project root mein `firebase-credentials.json` naam se save karo
4. Agar ye step skip kiya, app bina kisi problem ke chalega, bas chatbot logs Firestore mein save nahi honge

## Step 7 — App run karo
```
python app.py
```
Terminal mein `* Running on http://127.0.0.1:5000` dikhega — Ctrl+Click karo ya browser mein type karo.

Pehli baar chalane pe HuggingFace se 2 models download honge (~100-200MB), internet chahiye, thoda time lagega.

## Naye features kahan hain
- **Chatbot:** navbar mein "🤖 Ask AI" pe click karo, ya seedha `http://127.0.0.1:5000/chatbot`
- **Location-based weather:** Disease detection page (`/disease-predict`) khologe to browser location permission maangega — allow karna
- **Naya sidebar dashboard:** login karne ke baad `/dashboard` pe — sab real working links (Disease/Crop/Fertilizer/Chatbot/Logout)
- **Naya naam + logo:** ArogyaKrishi se FarmVision, poora rebrand + naya unique logo (`branding/` folder mein SVG+PNG)

## Agar koi error aaye
Terminal ka poora error message/screenshot bhej dena, fix kar denge.
