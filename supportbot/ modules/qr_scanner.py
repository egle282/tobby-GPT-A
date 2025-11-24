python
from pyzbar.pyzbar import decode
from PIL import Image
import io

class QRScanner:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('qr_scanner'):
            return False
        # Только если есть фото
        if msg.content_type == 'photo':
            try:
                file_id = msg.photo[-1].file_id
                file_info = self.bot.get_file(file_id)
                downloaded = self.bot.download_file(file_info.file_path)
                img = Image.open(io.BytesIO(downloaded))
                qr_codes = decode(img)
                if qr_codes:
                    for obj in qr_codes:
                        self.bot.send_message(msg.chat.id, f"Найден код: {obj.data.decode()}")
                else:
                    self.bot.send_message(msg.chat.id, "QR-код/штрихкод не обнаружен.")
                return True
            except Exception as e:
                self.bot.send_message(msg.chat.id, "Ошибка при распознавании QR/штрихкода.")
                print(e)
                return True
        return False
