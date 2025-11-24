python
class FileModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('file_module'): return False
        if msg.content_type not in ['document','photo']:
            return False
        self.bot.send_message(msg.chat.id, "Файл получен. Оператор сможет его посмотреть.")
        # Здесь логика сохранения/пересылки
        return True
