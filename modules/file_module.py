"""
Модуль отвечает за простую передачу файлов или фотографий от пользователя в бот.
После активации (например, через нажатие нужной кнопки) бот ожидает файл любого типа —
документ, фото или архив. Получив файл, бот подтверждает это сообщением.
Модуль может быть использован для сбора заявок, документов, скриншотов и других вложений.
Удобно использовать для сбора информации, обратной связи, обмена файлами с поддержкой.
"""
class FileModule:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_file = set()

    def handle(self, msg):
        if not self.is_enabled('file_module'):
            return False

        if msg.text == "📎 Файл":
            self.await_file.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Жду ваш файл (документ, фото, архив и т.д.)!")
            return True
            if msg.from_user.id in self.await_file:
            if msg.content_type == "document":
                self.await_file.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, f"Файл '{msg.document.file_name}' успешно получен!")
                return True
            elif msg.content_type == "photo":
                self.await_file.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, "Фото получено!")
                return True
            else:
                self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте файл или фото!")
                return True

        return False
