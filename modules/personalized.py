"""
Модуль для выдачи персонализированных автоответов на основе истории пользователя.
Использует последние сообщения пользователя для более релевантной поддержки.
"""

import json
from config import HISTORY_FILE

class Personalized:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        self.history_file = HISTORY_FILE

    def handle(self, msg):
        """
        Проверяет, задавал ли пользователь аналогичный вопрос ранее, и предлагает помощь.
        """
        if not self.feature_on('personalized'):
            return False
        try:
            with open(self.history_file, 'r', encoding='utf8') as f:
                hist = json.load(f)
        except Exception:
            hist = {}
        usr = str(msg.from_user.id)
        last = hist.get(usr, [])
        if last and msg.text and any('оплат' in q for q in last):
            self.bot.send_message(
                msg.chat.id,
                "В прошлый раз вы спрашивали о платеже. Напомнить как оплатить?"
            )
            return True
        return False
