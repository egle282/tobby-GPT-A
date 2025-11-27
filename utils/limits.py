import json
import time
from config import FREE_TEST_MODE, ADMINS
from utils.subscription import check_subscription

HISTORY_FILE = 'data/user_history.json'
FREE_LIMIT = 5  # сколько действий бесплатно в сутки

def get_today() -> str:
    return time.strftime('%Y-%m-%d')

def get_user_count(user_id: int) -> int:
    """Возвращает сколько сегодня пользователь совершил попыток"""
    try:
        with open(HISTORY_FILE, encoding='utf-8') as f:
            history = json.load(f)
    except Exception:
        history = {}
    uid = str(user_id)
    today = get_today()
    return history.get(uid, {}).get(today, 0)
def add_user_action(user_id: int):
    """Увеличивает счетчик действий за сегодня для пользователя"""
    try:
        with open(HISTORY_FILE, encoding='utf-8') as f:
            history = json.load(f)
    except Exception:
        history = {}
    uid = str(user_id)
    today = get_today()
    if uid not in history:
        history[uid] = {}
    if today not in history[uid]:
        history[uid][today] = 0
    history[uid][today] += 1
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f)

def can_use_feature(user_id: int) -> bool:
    """Проверяет разрешено ли ещё использовать платную фичу"""
    if FREE_TEST_MODE or user_id in ADMINS or check_subscription(user_id):
        return True  # нет ограничений
    return get_user_count(user_id) < FREE_LIMIT
