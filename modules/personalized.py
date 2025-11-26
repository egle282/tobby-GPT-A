"""
Модуль для персонализации обращения бота к каждому пользователю.
После активации бот предложит ввести желаемое имя или псевдоним, под которым будет обращаться к пользователю в будущем.
Это добавляет ботам “человеческое лицо”, улучшает качество коммуникации и помогает строить более дружелюбный диалог.
"""
class Personalized:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_pers = set()
        self.user_names = {}

    def handle(self, msg):
        if not self.is_enabled('personalized'):
            return False
        if msg.text == "✨ Персонализация":
            self.await_pers.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Как вас называть? Напишите желаемое имя/ник.")
            return True
        if msg.from_user.id in self.await_pers:
            name = (msg.text or "").strip()
            if name:
                self.user_names[msg.from_user.id] = name
                self.bot.send_message(msg.chat.id, f"Теперь я буду обращаться к вам: {name}")
                self.await_pers.remove(msg.from_user.id)
            else:
                self.bot.send_message(msg.chat.id, "Имя не распознано. Пожалуйста, введите ещё раз.")
            return True
        return False
