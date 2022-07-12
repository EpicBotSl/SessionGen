import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_URI = os.getenv("MONGO_URI", "").strip()
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL", "").strip()
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "").strip()
