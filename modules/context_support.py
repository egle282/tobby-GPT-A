"""
Модуль для хранения истории обращений пользователя (до 10 последних сообщений).
Используется для персонализации автоответов, анализа и построения контекста ответа.
"""

class ContextSupport:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.waiting_support_msg = set()
        def handle(self, msg):
        if not self.feature_on('context_support'):
            return False
        if msg.text == "💬 Поддержка":
            self.waiting_support_msg.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Опишите вашу проблему или вопрос, и мы скоро свяжемся с вами.")
            return True
        if msg.from_user.id in self.waiting_support_msg and msg.text:
            self.waiting_support_msg.remove(msg.from_user.id)
            # Здесь отправляется сообщение админу, например:
            # self.bot.send_message(ADMIN_ID, f"Новое обращение от @{msg.from_user.username} ({msg.chat.id}):\n{msg.text}")
            self.bot.send_message(msg.chat.id, "Спасибо! Обращение отправлено специалисту, скоро свяжемся с вами.")
            return True
        if msg.from_user.id in self.waiting_support_msg:
            self.bot.send_message(msg.chat.id, "Пожалуйста, опишите проблему текстом.")
            return True
        return False
