"""
Модуль мультиязычия.
Позволяет пользователю установить язык через команду /lang XX, автоматически переводит вопросы и ответы.
Использует Google Translate.
"""
class MultiLang:
    def __init__(self, bot, is_enabled_cb, supported=None):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_lang_choice = set()
        self.user_lang = {}
        self.supported = supported or {"RU": "Русский", "EN": "English", "ES": "Español"}
        def handle(self, msg):
        if not self.is_enabled('multilang'):
            return False
        if msg.text == "🌐 Язык":
            self.await_lang_choice.add(msg.from_user.id)
            langs = "\n".join([f"{k}: {v}" for k,v in self.supported.items()])
            self.bot.send_message(msg.chat.id, f"Выберите язык, отправив его код:\n{langs}")
            return True
        if msg.from_user.id in self.await_lang_choice:
            code = msg.text.upper().strip() if msg.text else ""
            if code in self.supported:
                self.user_lang[msg.from_user.id] = code
                self.await_lang_choice.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, f"Язык установлен: {self.supported[code]}")
            else:
                self.bot.send_message(msg.chat.id, "Некорректный код языка. Попробуйте заново. Доступно:\n" +
                                      ", ".join(self.supported.keys()))
            return True
        return False
