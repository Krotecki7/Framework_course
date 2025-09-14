from celery import shared_task


BOT_TOKEN = os.getenv(TG_BOT_TOKEN)
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


@shared_task
def send_notification(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    try:
        request.get(BASE_URL, params=params)
    except Exception as e:
        print(f"ошибка {e}")
