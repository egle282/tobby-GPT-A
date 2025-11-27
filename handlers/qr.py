from loader import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_qr, kb_main
from modules.qr_scanner import QRScanner

qr_module = QRScanner(bot)

@bot.message_handler(func=lambda m: m.text == "📷 QR-сканер")
def qr_start(msg):
    bot.send_message(msg.chat.id, "Сделайте фото QR-кода или загрузите его.", reply_markup=kb_qr())
    set_state(msg.from_user.id, "wait_qr_photo")

@bot.message_handler(func=lambda m: m.text == "Сделать фото сразу")
def stub_camera(msg):
    bot.send_message(msg.chat.id, "⏳ Функция съёмки пока недоступна. Просто загрузите фото с QR вручную.")
@bot.message_handler(content_types=['photo'])
def handle_qr(msg):
    if get_state(msg.from_user.id) == "wait_qr_photo":
        result = qr_module.handle(msg)  # Подключи сам обработчик QR в modules/qr_scanner.py
        reply = result or "QR-код не распознан или функция недоступна."
        bot.send_message(msg.chat.id, reply, reply_markup=kb_main())
        clear_state(msg.from_user.id)
