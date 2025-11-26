"""
Позволяет пользователю отправить e-mail в поддержку через команду /email.
"""
class SendEmail:
    def __init__(self, bot, is_enabled_cb, admin_email):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.admin_email = admin_email
        self.awaiting_email = set()

    def handle(self, msg):
        if not self.is_enabled('send_email'):
            return False

        if msg.text == "Отправить Email":
            self.awaiting_email.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Введите текст письма — мы отправим его в поддержку.")
            return True

        if msg.from_user.id in self.awaiting_email:
            if msg.text:
                self.awaiting_email.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, f"Ваш текст:\n{msg.text}\n\nотправлен на {self.admin_email}")
                return True
            else:
                self.bot.send_message(msg.chat.id, "Жду текст письма, отправьте ещё раз.")
                return True

        return False
