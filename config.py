import os
from dotenv import load_dotenv

load_dotenv()

# Weather API key, loaded from .env (OPEN_WEATHER_APIKEY=...)
weather_api_key = os.getenv("OPEN_WEATHER_APIKEY", "")
