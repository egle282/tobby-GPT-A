"""
Модуль для сбора оценок и отзывов о работе бота или сервиса в удобной для пользователя форме.
Показывает кнопки с “звёздочками”, пользователь выбирает вариант, а бот фиксирует выбранную оценку
и благодарит пользователя за обратную связь.
Применяется для мониторинга качества работы поддержки, автоматизации реферальных программ и получения отзывов.
"""
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class FeedbackReferral:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb

    def handle(self, msg):
        if not self.is_enabled('feedback_referral'):
            return False

        if msg.text == "Оценить":
            kb = InlineKeyboardMarkup(row_width=5)
            for i in range(1, 6):
                kb.add(InlineKeyboardButton("⭐️" * i, callback_data=f"fb_{i}"))
            self.bot.send_message(msg.chat.id, "Пожалуйста, оцените нашу работу:", reply_markup=kb)
            return True

        return False
