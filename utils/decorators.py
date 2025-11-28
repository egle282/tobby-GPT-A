# utils/decorators.py
from functools import wraps
from telebot.types import Message

def require_subscription(check_func):
    """
    Декоратор: пропускает обработчик, если check_func(user_id) == True.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(message: Message, *args, **kwargs):
            if check_func(message.from_user.id):
                return func(message, *args, **kwargs)
            else:
                message.bot.send_message(message.chat.id, "❗ Эта команда доступна только с подпиской.")
        return wrapper
    return decorator

def require_admin(check_func):
    """
    Декоратор: пропускает обработчик для админов.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(message: Message, *args, **kwargs):
            if check_func(message.from_user.id):
                return func(message, *args, **kwargs)
            else:
                message.bot.send_message(message.chat.id, "⛔ Только для администраторов.")
        return wrapper
    return decorator

def logger(func):
    """
    Логгер вызова функций.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
