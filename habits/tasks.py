import requests
from celery import shared_task
import os
from dotenv import load_dotenv
from django.utils import timezone


load_dotenv()


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_notification(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    try:
        requests.post(BASE_URL, params=params)
    except Exception as e:
        print(f"ошибка {e}")


@shared_task
def send_habit_reminders():

    now = timezone.now().time()

    habits = Habit.objects.filter(is_public=True).select_related("user")

    for habit in habits:
        chat_id = getattr(habit.user, "chat_id", None)
        if chat_id and habit.time <= now:
            message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"
            send_notification(chat_id, message)
