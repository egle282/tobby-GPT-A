"""
Модуль для интерактивного приёма голосовых сообщений пользователя.
После запуска этой функции бот ожидает, что пользователь отправит ему голосовое сообщение.
После получения бот подтверждает приём голосового.
Можно легко расширить модуль для распознавания речи и дальнейшей обработки содержимого голосовых сообщений.
Это открывает удобный канал для менее формализованных запросов и обратной связи.
**Особенности:**  
- Обрабатывает как голосовые, так и аудиофайлы пользователя.
- Реальное распознавание речи через Google.
- Удаляет временные файлы.
- Сообщает об ошибке, если что-то пошло не так.
"""
import os
import requests
from pydub import AudioSegment
import speech_recognition as sr

class VoiceModule:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_voice = set()
        self.recognizer = sr.Recognizer()

    def download_file(self, file_id, filename):
        file_info = self.bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{self.bot.token}/{file_info.file_path}"
        r = requests.get(file_url)
        with open(filename, "wb") as f:
            f.write(r.content)

    def recognize_file(self, filename, ext):
        base, _ = os.path.splitext(filename)
        wav_filename = base + ".wav"
        # Конвертация в WAV
        if ext == ".ogg":
            sound = AudioSegment.from_ogg(filename)
            sound.export(wav_filename, format="wav")
            filename = wav_filename
        elif ext == ".mp3":
            sound = AudioSegment.from_mp3(filename)
            sound.export(wav_filename, format="wav")
            filename = wav_filename
        # Распознавание речи
        with sr.AudioFile(filename) as source:
            audio = self.recognizer.record(source)
        text = self.recognizer.recognize_google(audio, language="ru-RU")
        return text

    def handle(self, msg):
        if not self.is_enabled('voice_module'):
            return False

        if getattr(msg, "text", None) == "🎤 Голосовое":
            self.await_voice.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Жду голосовое или аудиофайл!")
            return True
        if msg.from_user.id in self.await_voice:
            content_type = getattr(msg, 'content_type', None)
            if content_type in ("voice", "audio"):
                file_id = msg.voice.file_id if content_type == "voice" else msg.audio.file_id
                ext = ".ogg" if content_type == "voice" else ".mp3"
                temp_name = f"audio_{msg.message_id}{ext}"
                try:
                    self.download_file(file_id, temp_name)
                    text = self.recognize_file(temp_name, ext)
                    self.bot.send_message(msg.chat.id, f"Распознанный текст: {text}")
                except Exception as e:
                    self.bot.send_message(msg.chat.id, f"Ошибка при распознавании: {e}")
                finally:
                    # Удаляем временные файлы
                    for postfix in (ext, ".wav"):
                        fn = f"audio_{msg.message_id}{postfix}"
                        if os.path.exists(fn):
                            os.remove(fn)
                self.await_voice.remove(msg.from_user.id)
            else:
                self.bot.send_message(
                    msg.chat.id, 
                    "Жду именно голосовое сообщение или аудиофайл."
                )
            return True

        return False
