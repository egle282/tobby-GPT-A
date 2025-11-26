"""
Модуль для подписки/рассылки новостей, обновлений, информационных сообщений.
Пользователь подписывается через ключевое слово ('новост'), сообщения рассылаются send_news(text).
"""
class Mailing:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_message = set()

    def handle(self, msg):
        if not self.is_enabled('mailing'):
            return False
        if msg.text == "📬 Рассылка":
            self.await_message.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Введите текст рассылки. ВНИМАНИЕ: он уйдёт всем пользователям!")
            return True
        if msg.from_user.id in self.await_message:
            text = (msg.text or "").strip()
            if text and len(text) > 3:
                self.await_message.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, f"Рассылка отправлена: {text[:64]}... (эмуляция)")
            else:
                self.bot.send_message(msg.chat.id, "Слишком короткий текст. Попробуйте ещё раз.")
            return True
        return False
