import requests
import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_notification(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    try:
        requests.post(BASE_URL, params=params)
    except Exception as e:
        print(f"ошибка {e}")

