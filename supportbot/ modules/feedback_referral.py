python
"""
feedback_referral.py
--------------------
Модуль сбора отзывов (оценивание бота, 1-5 звезд) и auto-referral — кнопка "Пригласить друга".
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class FeedbackReferral:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        def handle(self, msg):
        """Вызывает инлайн-клавиатуру для оставления оценки и получения реферальной ссылки."""
        if not self.feature_on('feedback_referral'):
            return False
        if msg.text and "оцен" in msg.text.lower():
            kb = InlineKeyboardMarkup()
            for i in range(1, 6):
                kb.add(InlineKeyboardButton(f'⭐️{i}', callback_data=f'fb_{i}'))
            kb.add(InlineKeyboardButton('🔗 Пригласить друга', switch_inline_query=''))
            self.bot.send_message(msg.chat.id, "Как вы оцениваете нашу работу?", reply_markup=kb)
            return True
        return False
