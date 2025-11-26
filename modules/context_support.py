"""
Модуль для хранения истории обращений пользователя (до 10 последних сообщений).
Используется для персонализации автоответов, анализа и построения контекста ответа.
"""
class ContextSupport:
    def __init__(self, bot, is_enabled_cb, admin_id=None):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_support = set()
        self.admin_id = admin_id

    def handle(self, msg):
        if not self.is_enabled('context_support'):
            return False

        if msg.text == "💬 Поддержка":
            self.await_support.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Опишите вашу проблему. Можно приложить скриншот или документ.")
            return True
            if msg.from_user.id in self.await_support:
            if msg.text:
                self.await_support.remove(msg.from_user.id)
                if self.admin_id:
                    self.bot.send_message(self.admin_id, f"Новое обращение от @{msg.from_user.username or msg.from_user.id}:\n{msg.text}")
                self.bot.send_message(msg.chat.id, "Спасибо! Ваше обращение отправлено.")
                return True
            else:
                self.bot.send_message(msg.chat.id, "Жду текст обращения.")
                return True

        return False
