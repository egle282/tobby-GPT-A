python
import json
from config import HISTORY_FILE

class Personalized:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.history_file = HISTORY_FILE

    def handle(self, msg):
        if not self.feature_on('personalized'):
            return False
        # Проверим в истории, какие были последние вопросы
        try:
            with open(self.history_file, 'r', encoding='utf8') as f:
                hist = json.load(f)
        except:
            hist = {}
        usr = str(msg.from_user.id)
        last = hist.get(usr, [])
        if last and msg.text and any('оплата' in q for q in last):
            self.bot.send_message(
                msg.chat.id,
                "В прошлый раз вы спрашивали о платеже. Нужно повторить инструкцию?"
            )
            return True
        return False
