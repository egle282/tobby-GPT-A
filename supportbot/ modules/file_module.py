python
class FileModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('file_module'):
            return False
        if msg.content_type == 'document':
            file_info = self.bot.get_file(msg.document.file_id)
            file_path = file_info.file_path
            # For demo: just inform user
            self.bot.send_message(msg.chat.id, "Файл получен и принят.")
            return True
        elif msg.content_type == 'photo':
            self.bot.send_message(msg.chat.id, "Фото получено и принято.")
            return True
        return False
