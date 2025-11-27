from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_qr, kb_main

@bot.message_handler(func=lambda m: m.text == "📷 QR-сканер")
def qr_start(msg):
    bot.send_message(msg.chat.id, "Сделайте фото QR или загрузите", reply_markup=kb_qr())
    set_state(msg.from_user.id, "wait_qr_photo")

@bot.message_handler(content_types=['photo'])
def handle_qr(msg):
    if get_state(msg.from_user.id) == "wait_qr_photo":
        # Тут интеграция с модулем qr_scanner
        bot.send_message(msg.chat.id, "QR обработан!", reply_markup=kb_main())
        clear_state(msg.from_user.id)
