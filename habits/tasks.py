from celery import shared_task
from django.utils import timezone
from .models import Habit
from .services import send_notification


@shared_task
def send_habit_reminders():

    now = timezone.now().time()

    habits = Habit.objects.filter(is_public=True).select_related("user")

    for habit in habits:
        chat_id = getattr(habit.user, "chat_id", None)
        if chat_id and habit.time <= now:
            message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"
            send_notification(chat_id, message)
