python
import json
from rapidfuzz import fuzz
class FAQSearch:
    def __init__(self, bot, feature_on_fn, path='data/faq.json'):
        self.bot = bot
        self.feature_on = feature_on_fn
        try:
            with open(path, 'r', encoding='utf8') as f:
                self.faq = json.load(f)
        except:
            self.faq = []
            bot.send_message(ADMIN_IDS[0], "Ошибка загрузки FAQ!")

    def handle(self, msg):
        if not self.feature_on('faq_search'): return False
        text = msg.text.strip().lower() if msg.content_type == 'text' else ""
        if not text: return False
        # Поиск по FAQ
        best = max(self.faq, key=lambda x: fuzz.ratio(text, x["q"].lower()), default=None)
        if best and fuzz.ratio(text, best["q"].lower()) > 60:
            self.bot.send_message(msg.chat.id, f"Q: {best['q']}\nA: {best['a']}")
            return True
        return False
