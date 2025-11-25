python
"""
file_module.py
--------------
Модуль для работы с файлами и фотографиями.
Сохраняет, уведомляет о получении, подготавливает файлы для оператора.
"""

class FileModule:
    def __init__(self, bot, feature_on_fn):
        """
        :param bot: объект telebot.TeleBot
        :param feature_on_fn: функция проверки статуса модуля
        """
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        """Обрабатывает входящий файл или фото, отправляет подтверждение пользователю."""
        if not self.feature_on('file_module'):
            return False
        if msg.content_type == 'document':
            self.bot.send_message(msg.chat.id, "Файл получен и принят.")
            return True
        elif msg.content_type == 'photo':
            self.bot.send_message(msg.chat.id, "Фото получено и принято.")
            return True
        return False

