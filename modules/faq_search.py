faq_search.py
-------------
"Умный" поиск по базе FAQ. Использует rapidfuzz для сравнения текста запроса с вопросами.
Предлагает наиболее релевантный ответ.
"""

import json
from rapidfuzz import fuzz
from config import FAQ_FILE, ADMIN_IDS

class FAQSearch:
    def __init__(self, bot, feature_on_fn, path=FAQ_FILE):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        :param path: путь к базе FAQ
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        try:
            with open(path, 'r', encoding='utf8') as f:
                self.faq = json.load(f)
        except:
            self.faq = []
            try:
                bot.send_message(ADMIN_IDS[0], "Ошибка загрузки FAQ!")
            except:
                pass

    def handle(self, msg):
        """Сравнивает запрос пользователя с base-FAQ, возвращает найденный релевантный ответ."""
        if not self.feature_on('faq_search'):
            return False
        text = (msg.text or '').lower()
        if not text:
            return False
        best = None
        best_score = 0
        for item in self.faq:
            score = fuzz.ratio(text, item["q"].lower())
            if score > best_score:
                best_score = score
                best = item
        if best and best_score > 60:
            self.bot.send_message(msg.chat.id, f"Q: {best['q']}\nA: {best['a']}")
            return True
        return False

