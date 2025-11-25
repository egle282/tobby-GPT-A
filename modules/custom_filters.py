python
"""
custom_filters.py
-----------------
Продвинутый фильтр: блокирует и сообщает о сообщениях с запрещёнными словами или условиями.
"""
STOPWORDS = {"бан", "спам", "оскорбление"}

class CustomFilters:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('custom_filters'):
            return False
        if msg.text and any(word in msg.text.lower() for word in STOPWORDS):
            self.bot.send_message(msg.chat.id, "Это сообщение нарушает правила и не будет обработано.")
            return True  # Прекращаем дальнейшую обработку
        # Ваши другие проверки — пример:   if len(msg.text) < 3: ...
        return False
``

