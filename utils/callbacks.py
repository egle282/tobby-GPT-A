# utils/callbacks.py

def always_true(*args, **kwargs):
    """Всегда возвращает True."""
    return True

def always_false(*args, **kwargs):
    """Всегда возвращает False."""
    return False

def is_subscriber(user_id, *args, **kwargs):
    """
    Проверка подписки: пример заглушки, всегда возвращает True.
    На практике реализуй тут проверку по user_id.
    """
    return True

def is_admin(user_id, *args, **kwargs):
    """
    Заглушка на проверку роли администратора.
    Сравнивай user_id с заданными ID админов.
    """
    ADMIN_IDS = [os.getenv("ADMIN_IDS")]  # замени на реальные ID
    return user_id in ADMIN_IDS
def is_beta_tester(user_id, *args, **kwargs):
    """Проверяет, является ли пользователь бета-тестером."""
    BETA_TESTERS = [12345, 67890]
    return user_id in BETA_TESTERS

def has_active_trial(user_id, *args, **kwargs):
    """Псевдозаглушка: у всех пользователей активный пробный период."""
    return True

def check_daily_limit(user_id, command, limit=3):
    """
    Псевдозаглушка для проверки, не исчерпан ли лимит на выполнение команды.
    В реальной версии должна связываться с хранилищем.
    """
    return True

def is_support(user_id, *args, **kwargs):
    """Проверяет, является ли пользователь поддержкой (support team)."""
    SUPPORT_IDS = [11111111, 22222222]  # подставь реальные ID
    return user_id in SUPPORT_IDS
