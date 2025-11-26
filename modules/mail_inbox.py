"""
Модуль предоставляет пользователю быстрый доступ к его входящим сообщениям.
Может быть интегрирован с почтовой системой или внутренним сервисом рассылок.
После активации показывает список писем/уведомлений, а при отсутствии новых уведомляет об этом.
Это помогает пользователю не пропустить важные сообщения и быть всегда в курсе событий.
"""
class MailInbox:
    def __init__(self, bot, is_enabled_cb, get_inbox_fn=None):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_inbox = set()
        self.get_inbox = get_inbox_fn or (lambda user: ["Письмо #1: Тестовое сообщение", "Письмо #2: Акция!"])

    def handle(self, msg):
        if not self.is_enabled('mail_inbox'):
            return False
        if msg.text == "📥 Входящие":
            self.await_inbox.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Получаю список писем... (отправьте любую фразу, чтобы просмотреть)")
            return True
        if msg.from_user.id in self.await_inbox:
            user_mails = self.get_inbox(msg.from_user.id)
            if user_mails:
                mails = "\n\n".join(user_mails[:5])
                self.bot.send_message(msg.chat.id, f"Ваши письма:\n\n{mails}")
            else:
                self.bot.send_message(msg.chat.id, "Нет новых писем.")
            self.await_inbox.remove(msg.from_user.id)
            return True
        return False
