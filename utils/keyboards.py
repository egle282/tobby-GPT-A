from telebot.types import ReplyKeyboardMarkup

def kb_main():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📎 Файл", "📷 QR-сканер")
    kb.add("📢 Новости", "🎤 Голосовое")
    kb.add("FAQ", "Отправить Email")
    kb.add("Главное меню")
    return kb

def kb_qr():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add("Сделать фото сразу", "Главное меню")
    return kb
