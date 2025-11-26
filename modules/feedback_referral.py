"""
Модуль сбора отзывов (оценивание бота, 1-5 звезд) и auto-referral — кнопка "Пригласить друга".
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class FeedbackReferral:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('feedback_referral'):
            return False
        if msg.text == "Оценить":
            kb = InlineKeyboardMarkup(row_width=5)
            kb.add(
                InlineKeyboardButton("⭐️", callback_data="fb_1"),
                InlineKeyboardButton("⭐️⭐️", callback_data="fb_2"),
                InlineKeyboardButton("⭐️⭐️⭐️", callback_data="fb_3"),
                InlineKeyboardButton("⭐️⭐️⭐️⭐️", callback_data="fb_4"),
                InlineKeyboardButton("⭐️⭐️⭐️⭐️⭐️", callback_data="fb_5"),
            )
            self.bot.send_message(msg.chat.id, "Пожалуйста, оцените нашу работу:", reply_markup=kb)
            return True
        return False
# Не забудь добавить отдельный @bot.callback_query_handler для коллбэков feedback!
