python
import json
from config import HISTORY_FILE

class ContextSupport:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.history_file = HISTORY_FILE

    def save_history(self, user_id, message):
        try:
            with open(self.history_file, 'r', encoding='utf8') as f:
                hist = json.load(f)
        except:
            hist = {}
        usr = str(user_id)
        hist.setdefault(usr, []).append(message)
        hist[usr] = hist[usr][-10:]  # Only last 10
        with open(self.history_file, 'w', encoding='utf8') as f:
            json.dump(hist, f)

    def handle(self, msg):
        if not self.feature_on('context_support'):
            return False
        self.save_history(msg.from_user.id, msg.text or 'non-text')
        # Не перехватываем сообщение, пробрасываем дальше.
        return False
