import json
import os
from config import FREE_TEST_MODE, ADMINS

SUBSCRIBERS_FILE = "data/subscribers.json"

def load_subscribers() -> list:
    """Возвращает список подписчиков. Если файла нет — создаёт его."""
    if not os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return []
    try:
        with open(SUBSCRIBERS_FILE, encoding='utf-8') as f:
            subs = json.load(f)
            return subs if isinstance(subs, list) else []
    except Exception as e:
        print(f"Ошибка чтения {SUBSCRIBERS_FILE}: {e}")
        return []

def save_subscribers(subs: list):
    """Сохраняет список подписчиков."""
    with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(subs, f)

def check_subscription(user_id: int) -> bool:
    """Проверяет есть ли у пользователя активная подписка."""
    if FREE_TEST_MODE or user_id in ADMINS:
        return True
    subs = load_subscribers()
    return str(user_id) in subs

def add_subscriber(user_id: int):
    """Добавляет пользователя в список подписчиков (админ-метод)."""
    subs = load_subscribers()
    uid = str(user_id)
    if uid not in subs:
        subs.append(uid)
        save_subscribers(subs)

def remove_subscriber(user_id: int):
    """Удаляет пользователя из подписчиков."""
    subs = load_subscribers()
    uid = str(user_id)
    if uid in subs:
        subs.remove(uid)
        save_subscribers(subs)
