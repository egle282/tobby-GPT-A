# utils/callbacks.py

def always_true(*args, **kwargs):
    """Заглушка: всегда возвращает True"""
    return True

def always_false(*args, **kwargs):
    """Заглушка: всегда возвращает False"""
    return False

def echo_args(*args, **kwargs):
    """Пример: просто возвращает переданные аргументы"""
    return args, kwargs
