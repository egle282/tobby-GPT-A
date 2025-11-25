python
"""
push_notify.py
--------------
Модуль push-уведомлений. Позволяет пользователям подписываться на обновления.
Push-уведомления рассылаются через вызов метода send_push(text) по всем подписчикам.
"""

class PushNotify:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        self.users = set()

    def handle(self, msg):
        """Позволяет подписаться на push через запрос содержаший 'подпис'. """
        if not self.feature_on('push_notify'):
            return False
        if msg.text and 'подпис' in msg.text.lower():
            self.users.add(msg.chat.id)
            self.bot.send_message(msg.chat.id, "Теперь вы будете получать push-уведомления!")
            return True
        return False

    def send_push(self, text):
        """Рассылает заданный текст по всем подписчикам."""
        for uid in self.users:
            try:
                self.bot.send_message(uid, f"🔔 {text}")
            except:
                pass

