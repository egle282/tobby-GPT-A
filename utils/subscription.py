import json
from config import FREE_TEST_MODE, ADMINS

SUBSCRIBERS_FILE = "data/subscribers.json"

def check_subscription(user_id: int) -> bool:
    """Проверяет есть ли у пользователя активная подписка."""
    # Разрешить всё, если тестовый режим
    if FREE_TEST_MODE or user_id in ADMINS:
        return True
    try:
        with open(SUBSCRIBERS_FILE, encoding='utf-8') as f:
            subs = json.load(f)
        return str(user_id) in subs
    except Exception:
        return False

def add_subscriber(user_id: int):
    """Добавляет пользователя в список подписчиков (админ-метод)."""
    try:
        with open(SUBSCRIBERS_FILE, encoding='utf-8') as f:
            subs = json.load(f)
    except Exception:
        subs = []
    uid = str(user_id)
    if uid not in subs:
        subs.append(uid)
        with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(subs, f)

def remove_subscriber(user_id: int):
    """Удаляет пользователя из подписчиков."""
    try:
        with open(SUBSCRIBERS_FILE, encoding='utf-8') as f:
            subs = json.load(f)
    except Exception:
        subs = []
    uid = str(user_id)
    if uid in subs:
        subs.remove(uid)
        with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(subs, f)
