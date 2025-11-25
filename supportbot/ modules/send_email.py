python
"""
send_email.py
-------------
Позволяет переслать сообщения пользователя на e-mail службы поддержки командой /email.
"""
import os, yagmail

SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
SUPPORT_SMTP_USER = os.getenv("SMTP_USER")
SUPPORT_SMTP_PASS = os.getenv("SMTP_PASS")

class SendEmail:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.client = yagmail.SMTP(user=SUPPORT_SMTP_USER, password=SUPPORT_SMTP_PASS)

    def handle(self, msg):
        if not self.feature_on('send_email'):
            return False
        if msg.text and msg.text.startswith("/email "):
            theme = "Запрос в поддержку " + str(msg.from_user.id)
            content = msg.text[len("/email "):]
            self.client.send(to=SUPPORT_EMAIL, subject=theme, contents=content)
            self.bot.send_message(msg.chat.id, "Ваше сообщение отправлено в поддержку на email!")
            return True
        return False
