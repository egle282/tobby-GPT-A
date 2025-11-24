```python
import telebot
from config import BOT_TOKEN, ADMIN_IDS
from modules.context_support import ContextSupport
from modules.file_module import FileModule
from modules.multilang import Multilang
from modules.personalized import Personalized
from modules.feedback_referral import FeedbackReferral
from modules.faq_search import FAQSearch
from modules.qr_scanner import QRScanner
from modules.push_notify import PushNotify
from modules.cross_platform import CrossPlatform
from modules.mailing import Mailing
from modules.ai_handler import AIHandler
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot(BOT_TOKEN)

# Глобальные настройки (можно сохранять в файл для персистентности)
modules_enabled = {
    "context_support": True,
    "file_module": True,
    "multilang": True,
    "personalized": True,
    "feedback_referral": True,
    "faq_search": True,
    "qr_scanner": True,
    "push_notify": True,
    "cross_platform": False,
    "mailing": True,
    "ai_handler": True,
}

def feature_on(name): return modules_enabled.get(name, False)

# Модули
context_support = ContextSupport(bot, feature_on)
file_module = FileModule(bot, feature_on)
multilang = Multilang(bot, feature_on)
personalized = Personalized(bot, feature_on)
feedback_referral = FeedbackReferral(bot, feature_on)
faq_search = FAQSearch(bot, feature_on)
qr_scanner = QRScanner(bot, feature_on)
push_notify = PushNotify(bot, feature_on)
cross_platform = CrossPlatform(bot, feature_on)
mailing = Mailing(bot, feature_on)
ai_handler = AIHandler(bot, feature_on)

# Главное меню
def gen_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🛈 FAQ"), KeyboardButton("💬 Поддержка"))
    kb.add(KeyboardButton("Отправить QR") if feature_on('qr_scanner') else None)
    kb.add(KeyboardButton("📎 Файл") if feature_on('file_module') else None)
    kb.add(KeyboardButton("Оценить" ) if feature_on('feedback_referral') else None)
    return kb

@bot.message_handler(commands=['start'])
def handle_start(msg):
    bot.send_message(
        msg.chat.id,
        'Добро пожаловать! Задайте вопрос либо используйте команды.',
        reply_markup=gen_menu()
    )

# Администрирование
@bot.message_handler(commands=['admin_toggle'])
def admin_toggle(msg):
    if msg.from_user.id not in ADMIN_IDS:
        bot.send_message(msg.chat.id, "Нет доступа")
        return
    try:
        _, mod, state = msg.text.lower().split()
        if mod not in modules_enabled:
            raise Exception
        modules_enabled[mod] = (state == 'on')
        bot.reply_to(msg, f"Модуль {mod} теперь {'включен' if state == 'on' else 'выключен'}")
    except Exception:
        bot.reply_to(msg, "Формат: /admin_toggle <module> <on/off>")

@bot.message_handler(content_types=['text','photo','document'])
def route(msg):
    # Все модули — приоритетно, далее fallback
    if file_module.handle(msg): return
    if qr_scanner.handle(msg): return
    if multilang.handle(msg): return
    if personalized.handle(msg): return
    if context_support.handle(msg): return
    if faq_search.handle(msg): return
    if ai_handler.handle(msg): return
    if feedback_referral.handle(msg): return
    bot.send_message(msg.chat.id, 'Ваш запрос на обработке! Используйте главное меню, чтобы ускорить ответ.')

bot.polling()
