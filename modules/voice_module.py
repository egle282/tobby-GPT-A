"""
Распознает голосовые сообщения с помощью SpeechRecognition, пересылает текст оператору/боту.
"""

class VoiceModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.expecting_voice = set()
        def handle(self, msg):
        if not self.feature_on('voice_module'):
            return False
        if msg.text == "🎤 Голосовое":
            self.expecting_voice.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте голосовое сообщение для обработки!")
            return True
        if msg.from_user.id in self.expecting_voice and msg.content_type == "voice":
            self.expecting_voice.remove(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Голосовое получено! (Расшифровка включится позже.)")
            return True
        if msg.from_user.id in self.expecting_voice:
            self.bot.send_message(msg.chat.id, "Жду именно голосовое сообщение.")
            return True
        return False
