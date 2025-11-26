"""
Модуль кроссплатформенности: быстро предоставляет ссылки на поддержку в других каналах (WhatsApp, VK, сайт).
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
