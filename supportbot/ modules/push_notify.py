```python
class PushNotify:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.users = set()

    def handle(self, msg):
        if not self.feature_on('push_notify'):
            return False
        if msg.text and 'подпис' in msg.text.lower():
            self.users.add(msg.chat.id)
            self.bot.send_message(msg.chat.id, "Теперь вы будете получать push-уведомления.")
            return True
        return False
# Для отправки уведомлений  
    def send_push(self, text):
        for uid in self.users:
            try:
                self.bot.send_message(uid, f"🔔 {text}")
            except:
                pass
