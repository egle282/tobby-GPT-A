"""
Распознает голосовые сообщения с помощью SpeechRecognition, пересылает текст оператору/боту.
"""
class VoiceModule:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_voice = set()
        def handle(self, msg):
        if not self.is_enabled('voice_module'):
            return False

        if msg.text == "🎤 Голосовое":
            self.await_voice.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Жду голосовое сообщение!")
            return True

        if msg.from_user.id in self.await_voice:
            if msg.content_type == "voice":
                self.await_voice.remove(msg.from_user.id)
                self.bot.send_message(msg.chat.id, "Голосовое получено. (Здесь можно добавить распознавание текста)")
                return True
            else:
                self.bot.send_message(msg.chat.id, "Жду именно голосовое сообщение.")
                return True

        return False
