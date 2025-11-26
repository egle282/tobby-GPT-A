"""
Модуль для работы с файлами и фотографиями.
Сохраняет, уведомляет о получении, подготавливает файлы для оператора.
"""

class FileModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.expecting_file = set()  # айди юзеров, кто активировал модуль

    def handle(self, msg):
        if not self.feature_on('file_module'):
            return False
        # 1) Нажал кнопку
        if msg.text == "📎 Файл":
            self.expecting_file.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте файл (документ) в ответ на это сообщение.")
            return True
        # 2) Отправил файл
        if msg.from_user.id in self.expecting_file and msg.content_type == "document":
            self.expecting_file.remove(msg.from_user.id)
            self.bot.send_message(msg.chat.id, f"Документ {msg.document.file_name} успешно получен, спасибо!")
            return True
        # 3) Прислал что-то не то
        if msg.from_user.id in self.expecting_file:
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте именно файл (документ)!")
            return True
        return False
