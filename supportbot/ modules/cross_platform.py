python
class CrossPlatform:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('cross_platform'):
            return False
        if msg.text and 'whatsapp' in msg.text.lower():
            self.bot.send_message(msg.chat.id, 'Для поддержки в WhatsApp: +79001234567\nИЛИ по ссылке: https://wa.me/79001234567')
            return True
        # Можно добавить оповещение о поддержке во VK/Viber/Site
        return False
