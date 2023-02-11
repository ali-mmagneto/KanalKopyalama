import os

APP_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
KANALLAR = list(set(x for x in os.environ.get("KANALLAR", "1276627253").split()))
KANALIM = os.environ.get("KANALIM", None)
