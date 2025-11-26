"""
Модуль push-уведомлений. Позволяет пользователям подписываться на обновления.
Push-уведомления рассылаются через вызов метода send_push(text) по всем подписчикам.
"""
class PushNotify:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb

    def handle(self, msg):
        if not self.is_enabled('push_notify'):
            return False

        if msg.text == "📢 Новости":
            self.bot.send_message(
                msg.chat.id, "📢 Последние новости:\n- Добавлен FAQ.\n- Появился QR-сканер.\n- Бот работает лучше!")
            return True

        return False
