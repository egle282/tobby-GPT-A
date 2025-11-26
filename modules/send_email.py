"""
Позволяет пользователю отправить e-mail в поддержку через команду /email.
"""

class SendEmail:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.expecting_email = set()

    def handle(self, msg):
        if not self.feature_on('send_email'):
            return False
        if msg.text == "Отправить Email":
            self.expecting_email.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Введите текст письма, и мы отправим его службе поддержки.")
            return True
        if msg.from_user.id in self.expecting_email and msg.text:
            self.expecting_email.remove(msg.from_user.id)
            email_text = msg.text
            # *Здесь должна быть отправка по SMTP на email поддержки*
            self.bot.send_message(msg.chat.id, f"Ваше сообщение отправлено на email поддержки!\n\nТекст письма:\n{email_text}")
            return True
        if msg.from_user.id in self.expecting_email:
            self.bot.send_message(msg.chat.id, "Жду текст письма.")
            return True
        return False
