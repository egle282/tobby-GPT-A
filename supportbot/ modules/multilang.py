```python
from googletrans import Translator

class Multilang:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.translator = Translator()
        self.user_langs = {}
      def handle(self, msg):
        if not self.feature_on('multilang'):
            return False
        user_id = msg.from_user.id
        # Check if language set
        if msg.text and msg.text.lower().startswith('/lang '):
            langcode = msg.text.split()[1]
            self.user_langs[user_id] = langcode
            self.bot.send_message(msg.chat.id, f"Язык переключен на {langcode}")
            return True
        # Example: если пользователь не на русском -- переводим ответ
        if user_id in self.user_langs and self.user_langs[user_id] != 'ru':
            translation = self.translator.translate(msg.text, dest=self.user_langs[user_id])
            self.bot.send_message(msg.chat.id, f"🈯 Перевод: {translation.text}")
            return True
        return False
