"""
Модуль для работы с файлами и фотографиями.
Сохраняет, уведомляет о получении, подготавливает файлы для оператора.
"""

class FileModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.expecting_file = set()
        def handle(self, msg):
        if not self.feature_on('file_module'):
            return False
        if msg.text == "📎 Файл":
            self.expecting_file.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте файл (документ) — поддерживаются PDF, DOCX, изображения и другие форматы.")
            return True
        if msg.from_user.id in self.expecting_file and msg.content_type == "document":
            self.expecting_file.remove(msg.from_user.id)
            self.bot.send_message(msg.chat.id, f"Документ {msg.document.file_name} успешно получен и отправлен на обработку.")
            return True
        if msg.from_user.id in self.expecting_file and msg.content_type in ("photo", ):
            self.expecting_file.remove(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Спасибо! Фото принято как файл и отправлено на обработку.")
            return True
        if msg.from_user.id in self.expecting_file:
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте именно файл (или фото), чтобы продолжить.")
            return True
        return False
