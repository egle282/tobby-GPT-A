python
class Mailing:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.subscribers = set()

    def handle(self, msg):
        if not self.feature_on('mailing'):
            return False
        if msg.text and 'новост' in msg.text.lower():
            self.subscribers.add(msg.chat.id)
            self.bot.send_message(msg.chat.id, "Вы подписались на новости сервиса.")
            return True
        return False

    def send_news(self, text):
        for uid in self.subscribers:
            try:
                self.bot.send_message(uid, f"📰 {text}")
            except:
                pass
