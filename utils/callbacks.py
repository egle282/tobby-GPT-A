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
    ADMIN_IDS = [12345678]  # замени на реальные ID
    return user_id in ADMIN_IDS
