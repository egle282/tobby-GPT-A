# utils/decorators.py
from functools import wraps

def restricted_access(check_func):
    """Декоратор для ограничения доступа к функциям по условию."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if check_func(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                # Если хочется отправлять сообщение через бота о запрете:
                msg = args[0] if args else None
                if hasattr(msg, 'chat') and hasattr(msg, 'bot'):
                    msg.bot.send_message(msg.chat.id, "⛔️ Доступ запрещён.")
                else:
                    print("⛔️ Доступ запрещён.")
        return wrapper
    return decorator

def simple_logger(func):
    """Простой декоратор-логгер."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызван {func.__name__} с args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
