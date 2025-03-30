import requests
from config.settings import TELEGRAM_BOT_ID


def send_tg_message(message, chat_id):
    """
    Отправка сообщения в TG
    """
    params = {"text": message, "chat_id": chat_id}
    requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_ID}/sendMessage", params=params
    )


def week_days(string_day):
    days = string_day.split(",")
    list_day = []
    for day in days:
        list_day.append(int(day))
    return list_day
