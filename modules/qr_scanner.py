"""
Этот модуль превращает бота в удобный сканер QR-кодов.
Пользователь выбирает соответствующую функцию и отправляет фотографию с QR-кодом.
Бот распознает содержимое QR и отправляет его в ответном сообщении.
Если QR-код распознать не удалось, пользователь получит подсказку попробовать снова с другим изображением.
Идеально подходит для автоматизации ввода ссылок, промокодов, билетов и других сценариев.
"""
import tempfile
from pyzbar.pyzbar import decode
from PIL import Image

class QRScanner:
    def __init__(self, bot, is_enabled_cb):
        self.bot = bot
        self.is_enabled = is_enabled_cb
        self.await_photo = set()

    def handle(self, msg):
        if not self.is_enabled('qr_scanner'):
            return False

        if msg.text == "📷 QR-сканер":
            self.await_photo.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Жду фото с QR-кодом для распознавания!")
            return True

        if msg.from_user.id in self.await_photo:
            if msg.content_type == "photo":
                self.await_photo.remove(msg.from_user.id)
                file_id = msg.photo[-1].file_id
                file_info = self.bot.get_file(file_id)
                downloaded_file = self.bot.download_file(file_info.file_path)
                with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
                    tmp.write(downloaded_file)
                    tmp.flush()
                    try:
                        im = Image.open(tmp.name)
                        qrs = decode(im)
                        if not qrs:
                            self.bot.send_message(msg.chat.id, "QR-код не найден. Попробуйте сделать фото крупнее.")
                        else:
                            result = "\n".join([qr.data.decode("utf-8") for qr in qrs])
                            self.bot.send_message(msg.chat.id, f"✅ Распознан QR:\n\n{result}")
                    except Exception as e:
                        self.bot.send_message(msg.chat.id, f"Ошибка обработки изображения:\n{e}")
                return True
            else:
                self.bot.send_message(msg.chat.id, "Жду именно фото с QR-кодом!")
                return True

        return False
