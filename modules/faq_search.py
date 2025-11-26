import json
from rapidfuzz import fuzz
from config import FAQ_FILE, ADMIN_IDS

class FAQSearch:
    def __init__(self, bot, feature_on_fn, path=FAQ_FILE):
        self.bot = bot
        self.feature_on = feature_on_fn
        try:
            with open(path, 'r', encoding='utf8') as f:
                self.faq = json.load(f)
        except Exception as e:
            self.faq = []
            try:
                bot.send_message(ADMIN_IDS[0], f"Ошибка загрузки FAQ! {e}")
            except Exception:
                pass

    def handle(self, msg):
        if not self.feature_on('faq_search'):
            return False
        text = (msg.text or '').strip()
        if not text:
            return False
        # Кнопка FAQ
        if text == "🛈 FAQ":
            faqs = [item.get("q", "") for item in self.faq[:10]]
            txt = "Вот часто задаваемые вопросы:\n" + "\n".join(
                f"{i+1}. {q}" for i, q in enumerate(faqs))
            txt += "\n\nНапиши свой вопрос — я попробую найти ответ автоматически."
            self.bot.send_message(msg.chat.id, txt)
            return True
        # Умный поиск по базе
        question = text.lower()
        best = None
        best_score = 0
        for item in self.faq:
            score = fuzz.ratio(question, item.get("q", "").lower())
            if score > best_score:
                best_score = score
                best = item
        if best and best_score > 60:
            self.bot.send_message(msg.chat.id, f"Q: {best.get('q', '')}\nA: {best.get('a', '')}")
            return True
        return False
