"""
Модуль для подписки/рассылки новостей, обновлений, информационных сообщений.
Пользователь подписывается через ключевое слово ('новост'), сообщения рассылаются send_news(text).
"""

class Mailing:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn
        self.subscribers = set()

    def handle(self, msg):
        """Добавляет пользователя в список подписчиков на новости (слово 'новост')."""
        if not self.feature_on('mailing'):
            return False
        if msg.text and 'новост' in msg.text.lower():
            self.subscribers.add(msg.chat.id)
            self.bot.send_message(msg.chat.id, "Вы подписались на новостную рассылку!")
            return True
        return False

    def send_news(self, text):
        """Рассылает новость всем подписчикам."""
        for uid in self.subscribers.copy():
            try:
                self.bot.send_message(uid, f"📰 {text}")
            except Exception:
                # Если возникла ошибка (например, юзер заблокировал бота), удалим из подписчиков
                self.subscribers.discard(uid)
