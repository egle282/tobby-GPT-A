"""
Модуль реализует простой фильтр для автоматической проверки сообщений пользователя на стоп-слова и запрещённый контент.
Полезен для предотвращения спама, нецензурной лексики или других нежелательных сообщений.
Пользователь отправляет свой текст, модуль анализирует его, если находит запрещённые слова — уведомляет пользователя.
Применяется для базовой предмодерации и соблюдения правил чата прямо в боте.
"""
class CustomFilters:
    def __init__(self, bot, is_enabled_cb, blacklist=None):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_check = set()
        self.blacklist = set(blacklist) if blacklist else set()

    def handle(self, msg):
        if not self.is_enabled('custom_filters'):
            return False

        if msg.text == "🔍 Проверка":
            self.await_check.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Введите сообщение для проверки на стоп-слова или спам.")
            return True

        if msg.from_user.id in self.await_check:
            text = (msg.text or "").lower()
            if any(w in text for w in self.blacklist):
                self.bot.send_message(msg.chat.id, "Сообщение содержит запрещённые слова!")
            else:
                self.bot.send_message(msg.chat.id, "Проверка пройдена, всё чисто.")
            self.await_check.remove(msg.from_user.id)
            return True

        return False
