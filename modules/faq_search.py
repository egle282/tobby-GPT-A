"""
Этот модуль позволяет пользователям удобно искать ответы на часто задаваемые вопросы (FAQ) внутри бота.
Пользователь может выбрать интересующий вопрос из предложенного списка популярных или просто ввести свой текст.
Система находит наиболее похожий вопрос в базе и выдает релевантный ответ в диалоге.
Если подходящего ответа не найдено, бот просит сформулировать вопрос иначе.
Это помогает быстро находить необходимую информацию и снижает нагрузку на живую поддержку.
"""
import json
from rapidfuzz import fuzz

class FAQSearch:
    def __init__(self, bot, is_enabled_cb, faq_path='faq.json'):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        try:
            with open('data/faq_path, "r", encoding="utf-8") as f:
                self.faq = json.load(f)
        except Exception as e:
            self.faq = []
            print(f'FAQ загрузка: {e}')
        self.awaiting_question = set()

    def handle(self, msg):
        if not self.is_enabled('faq_search'):
            return False

        if msg.text == "🛈 FAQ":
            self.awaiting_question.add(msg.from_user.id)
            txt = "Задайте ваш вопрос, или выберите из популярных:\n\n"
            for i, item in enumerate(self.faq[:5]):
                txt += f"{i+1}. {item.get('q','')}\n"
            txt += "\nМожно просто написать свой вопрос, я попробую найти ответ."
            self.bot.send_message(msg.chat.id, txt)
            return True

        if msg.from_user.id in self.awaiting_question and msg.text:
            question = msg.text.lower()
            best = None
            best_score = 0
            for item in self.faq:
                score = fuzz.ratio(question, item.get("q", "").lower())
                if score > best_score:
                    best_score = score
                    best = item
            self.awaiting_question.remove(msg.from_user.id)
            if best and best_score > 60:
                self.bot.send_message(msg.chat.id, f"<b>Вопрос:</b> {best.get('q','')}\n\n<b>Ответ:</b> {best.get('a','')}", parse_mode="HTML")
            else:
                self.bot.send_message(msg.chat.id, "К сожалению, не найдено подходящего ответа. Попробуйте сформулировать иначе!")
            return True

        if msg.from_user.id in self.awaiting_question:
            self.bot.send_message(msg.chat.id, "Жду ваш вопрос по FAQ текстом!")
            return True

        return False
