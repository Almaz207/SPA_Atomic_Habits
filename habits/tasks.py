from celery import shared_task
from habits.models import Habit
from habits.services import send_tg_message, week_days
from datetime import datetime


@shared_task
def send_message_to_user():
    """
    Отправка напоминания
    """
    habits = Habit.objects.filter(pleasant_habit=False)

    now_day = datetime.now().isoweekday()

    for habit in habits:

        if now_day in week_days(habit.frequency):
            if habit.owner.telegram_id:
                message = f"У вас сегодня выполнение привычки: {habit.action}, которую нужно выполнить в {habit.time} в {habit.place}"
                send_tg_message(message=message, chat_id=habit.owner.telegram_id)
