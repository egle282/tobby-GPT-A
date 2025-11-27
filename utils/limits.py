import json
import os
import time
from config import FREE_TEST_MODE, ADMINS, FEATURE_LIMITS
from utils.subscription import check_subscription

HISTORY_FILE = 'data/user_history.json'

def get_today() -> str:
    """Возвращает текущую дату в формате ГГГГ-ММ-ДД."""
    return time.strftime('%Y-%m-%d')

def load_history() -> dict:
    """Загружает историю использования функций."""
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)
        return {}
    try:
        with open(HISTORY_FILE, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_history(history: dict):
    """Сохраняет историю использования функций."""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f)

def get_user_count(user_id: int, feature: str) -> int:
    """Возвращает сколько раз юзер сегодня использовал feature."""
    history = load_history()
    uid = str(user_id)
    today = get_today()
    return history.get(uid, {}).get(today, {}).get(feature, 0)

def add_user_action(user_id: int, feature: str):
    """Добавляет действие по feature для пользователя за сегодня."""
    history = load_history()
    uid = str(user_id)
    today = get_today()
    if uid not in history:
        history[uid] = {}
    if today not in history[uid]:
        history[uid][today] = {}
    if feature not in history[uid][today]:
        history[uid][today][feature] = 0
    history[uid][today][feature] += 1
    save_history(history)

def can_use_feature(user_id: int, feature: str) -> bool:
    """
    Проверяет, может ли пользователь воспользоваться функцией feature ещё раз сегодня.
    Для подписчиков и админов всегда True.
    """
    if FREE_TEST_MODE or user_id in ADMINS or check_subscription(user_id):
        return True
    # Получаем лимит для фичи из конфига, если его нет — по умолчанию 0
    limit = FEATURE_LIMITS.get(feature, 0)
    if limit == 0:
        return False  # Вообще нельзя незарегистрированным
    return get_user_count(user_id, feature) < limit
