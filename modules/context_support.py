context_support.py
-------------------
Модуль для хранения истории обращений пользователя (до 10 последних сообщений).
Используется для персонализации автоответов, анализа и построения контекста ответа.
"""

import json
from config import HISTORY_FILE

class ContextSupport:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        self.history_file = HISTORY_FILE

    def save_history(self, user_id, message):
        """
        Сохраняет последнее сообщение пользователя в файл истории.
        """
        try:
            with open(self.history_file, 'r', encoding='utf8') as f:
                hist = json.load(f)
        except:
            hist = {}
        usr = str(user_id)
        hist.setdefault(usr, []).append(message)
        hist[usr] = hist[usr][-10:]  # Only last 10
        with open(self.history_file, 'w', encoding='utf8') as f:
            json.dump(hist, f)

    def handle(self, msg):
        """
        Обрабатывает входящее сообщение, добавляет его в историю пользователя.
        """
        if not self.feature_on('context_support'):
            return False
        self.save_history(msg.from_user.id, msg.text or 'non-text')
        return False  # Контекст — вспомогательный модуль, не перехватывает сообщения

