"""
Позволяет пользователю отправить e-mail в поддержку через команду /email.
"""

import yagmail
from config import *

class SendEmail:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        try:
            self.client = yagmail.SMTP(user=SMTP_USER, password=SMTP_PASS)
        except Exception as e:
            self.client = None
            print("Не удалось подключиться к SMTP:", e)

    def handle(self, msg):
        """
        Если включено, позволяет отправить email через команду /email ...
        """
        if not self.feature_on('send_email'):
            return False
        if msg.text and msg.text.lower().startswith("/email "):
            if not SUPPORT_EMAIL or not SMTP_USER or not SMTP_PASS or not self.client:
                self.bot.send_message(msg.chat.id, "Отправка email временно недоступна.")
                return True
            subject = f"Бот Helpino, запрос от {msg.from_user.id}"
            text = msg.text[len("/email "):]
            try:
                self.client.send(to=SUPPORT_EMAIL, subject=subject, contents=text)
                self.bot.send_message(msg.chat.id, "Ваше сообщение отправлено в службу поддержки по email.")
            except Exception as e:
                self.bot.send_message(msg.chat.id, "Ошибка отправки email.")
                print("SMTP error:", e)
            return True
        return False
