"""
Модуль реализует возможность общения пользователя с внешним искусственным интеллектом (например, на базе GPT).
Пользователь задает вопрос, а бот отправляет его в AI и возвращает ответ.
Это позволяет пользователям получать быстрые консультации, советы или решения без обращения к оператору.
Подходит для “умного” FAQ, консультаций и автореспондера.
"""
class AIHandler:
    def __init__(self, bot, is_enabled_cb, ai_func=None):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_ai_question = set()
        self.ai_func = ai_func or (lambda prompt, user: "AI ответ: " + prompt)
        def handle(self, msg):
        if not self.is_enabled('ai_handler'):
            return False
        if msg.text == "🤖 Chat AI":
            self.await_ai_question.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Задайте любой вопрос искусственному интеллекту.")
            return True
        if msg.from_user.id in self.await_ai_question:
            question = (msg.text or "").strip()
            if question:
                answer = self.ai_func(question, msg.from_user.id)
                self.bot.send_message(msg.chat.id, answer)
                self.await_ai_question.remove(msg.from_user.id)
            else:
                self.bot.send_message(msg.chat.id, "Ваш вопрос пуст. Напишите вопрос для AI.")
            return True
        return False
