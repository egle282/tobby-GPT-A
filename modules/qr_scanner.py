"""
Принимает фотографии, распознаёт QR и штрих-коды в них с помощью pyzbar + Pillow.
Возвращает результат пользователю.
"""

import tempfile
from pyzbar.pyzbar import decode
from PIL import Image

class QRScanner:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.expecting_photo = set()

    def handle(self, msg):
        if not self.feature_on('qr_scanner'):
            return False
        # Ждет команду на старт сканера
        if msg.text == "📷 QR-сканер":
            self.expecting_photo.add(msg.from_user.id)
            self.bot.send_message(msg.chat.id, "Пожалуйста, отправьте фото с QR-кодом для распознавания!")
            return True
        # Ждет фото от пользователя
        if msg.from_user.id in self.expecting_photo and msg.content_type == "photo":
            self.expecting_photo.remove(msg.from_user.id)
            # Скачиваем файл
            file_id = msg.photo[-1].file_id  # берем самое большое фото
            file_info = self.bot.get_file(file_id)
            downloaded_file = self.bot.download_file(file_info.file_path)
            # Используем временный файл
            with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
                tmp.write(downloaded_file)
                tmp.flush()
                try:
                    image = Image.open(tmp.name)
                    qr_codes = decode(image)
                    if not qr_codes:
                        self.bot.send_message(msg.chat.id, "QR-код не найден или не распознан. Попробуйте другое фото.")
                    else:
                        results = []
                        for code in qr_codes:
                            code_data = code.data.decode('utf-8')
                            results.append(code_data)
                        result_text = "\n\n".join(results)
                        self.bot.send_message(msg.chat.id, f"✅ QR-код успешно распознан!\n\n{result_text}")
                except Exception as e:
                    self.bot.send_message(msg.chat.id, f"Ошибка при обработке изображения: {e}")
            return True
        # Не тот тип данных, просим еще фото
        if msg.from_user.id in self.expecting_photo:
            self.bot.send_message(msg.chat.id, "Жду фотографию с QR-кодом, пожалуйста попробуйте еще раз.")
            return True
        return False
