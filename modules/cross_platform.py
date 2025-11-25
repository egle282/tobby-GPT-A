"""
Модуль кроссплатформенности: быстро предоставляет ссылки на поддержку в других каналах (WhatsApp, VK, сайт).
"""

class CrossPlatform:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        """Предоставляет ссылки на поддержку в других платформах по ключевым словам."""
        if not self.feature_on('cross_platform'):
            return False
        if msg.text and 'whatsapp' in msg.text.lower():
            self.bot.send_message(msg.chat.id, 'Поддержка в WhatsApp: https://wa.me/79001234567')
            return True
        if msg.text and 'vk' in msg.text.lower():
            self.bot.send_message(msg.chat.id, 'VK: https://vk.com/support')
            return True
        if msg.text and 'сайт' in msg.text.lower():
            self.bot.send_message(msg.chat.id, 'Сайт поддержки: https://support.example.com')
            return True
        return False
