"""
Этот модуль помогает пользователю получить инструкции или полезную информацию
по работе сервиса на других платформах (например, Web, iOS, Android).
Пользователь просто указывает интересующую платформу, бот отвечает подходящей справкой или ссылкой.
Это значительно облегчает onboarding и работу с продуктом для пользователей на разных устройствах.
"""
class CrossPlatform:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_info = set()
        def handle(self, msg):
        if not self.is_enabled('cross_platform'):
            return False
        if msg.text == "🌍 Другая платформа":
            self.await_info.add(msg.from_user.id)
            self.bot.send_message(
                msg.chat.id,
                "Введите, с какой платформы вы хотите получить инструкции (например: Web, iOS, Android)."
            )
            return True
        if msg.from_user.id in self.await_info:
            platform = (msg.text or "").strip().lower()
            if platform in ("web", "ios", "android"):
                self.bot.send_message(msg.chat.id, f"Инструкции для {platform} платформы: (здесь будет текст для {platform})")
                self.await_info.remove(msg.from_user.id)
            else:
                self.bot.send_message(msg.chat.id, "Платформа не распознана. Доступно: Web, iOS, Android.")
            return True
        return False
