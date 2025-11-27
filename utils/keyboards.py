from telebot.types import ReplyKeyboardMarkup, KeyboardButton

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

def kb_location():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("Отправить местоположение", request_location=True))
    kb.add("Ввести город вручную")
    kb.add("Главное меню")
    return kb
