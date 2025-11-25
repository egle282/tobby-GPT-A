voice_module.py
---------------
Распознает голосовые сообщения с помощью SpeechRecognition, пересылает текст оператору/боту.
"""
import speech_recognition as sr
from pydub import AudioSegment
import os, io

class VoiceModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.rec = sr.Recognizer()
      def handle(self, msg):
        if not self.feature_on('voice_module'):
            return False
        if msg.content_type == 'voice':
            try:
                file_id = msg.voice.file_id
                file_info = self.bot.get_file(file_id)
                ogg_data = self.bot.download_file(file_info.file_path)
                audio = AudioSegment.from_file(io.BytesIO(ogg_data), format="ogg")
                wav_io = io.BytesIO()
                audio.export(wav_io, format="wav")
                wav_io.seek(0)
                with sr.AudioFile(wav_io) as source:
                    audio_data = self.rec.record(source)
                    text = self.rec.recognize_google(audio_data, language="ru-RU")
                self.bot.send_message(msg.chat.id, f"Распознано: {text}")
                # Можно отправить оператору, или обработать автоответ
                return True
            except Exception as e:
                self.bot.send_message(msg.chat.id, "Не разобрал :(")
                print(e)
                return True
        return False

