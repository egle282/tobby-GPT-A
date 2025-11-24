```python
import telebot
from config import BOT_TOKEN, ADMIN_IDS
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

# Импорт модулей
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

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

modules_enabled = {
    "context_support": True,
    "file_module": True,
    "multilang": True,
    "personalized": True,
    "feedback_referral": True,
    "faq_search": True,
    "qr_scanner": True,
    "push_notify": True,
    "cross_platform": True,
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

def gen_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🛈 FAQ"), KeyboardButton("💬 Поддержка"))
    if feature_on('file_module'):
        kb.add(KeyboardButton("📎 Файл"))
    if feature_on('qr_scanner'):
        kb.add(KeyboardButton("📷 QR-сканер"))
    if feature_on('mailing'):
        kb.add(KeyboardButton("📢 Новости"))
    if feature_on('feedback_referral'):
        kb.add(KeyboardButton("Оценить"))
    return kb

@bot.message_handler(commands=['start'])
def handle_start(msg):
    bot.send_message(
        msg.chat.id,
        f'Привет! Я бот поддержки. Спроси или воспользуйся меню:',
        reply_markup=gen_menu()
    )
    # Управление модулями
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
        bot.send_message(msg.chat.id, f"Модуль {mod} теперь {'включен' if state == 'on' else 'выключен'}")
    except Exception as e:
        bot.send_message(msg.chat.id, "Формат: /admin_toggle module on/off")

# Отклики с инлайн-оценкой
@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('fb_'))
def handle_feedback(call):
    stars = call.data[3:]
    bot.answer_callback_query(call.id, f"Спасибо за {stars}⭐️!")
    bot.send_message(call.from_user.id, "Спасибо за вашу оценку!")

# Главный роутер: каждый модуль в порядке приоритета
@bot.message_handler(content_types=['text', 'photo', 'document'])
def router(msg):
    if context_support.handle(msg): return
    if file_module.handle(msg): return
    if multilang.handle(msg): return
    if personalized.handle(msg): return
    if feedback_referral.handle(msg): return
    if faq_search.handle(msg): return
    if qr_scanner.handle(msg): return
    if push_notify.handle(msg): return
    if cross_platform.handle(msg): return
    if mailing.handle(msg): return
    if ai_handler.handle(msg): return
    bot.send_message(msg.chat.id, "Ваш запрос в очереди! Для ускорения выберите задачу из меню.")

if __name__ == '__main__':
    print("Стартую SupportBot!")  # Для мониторинга на Render
    bot.infinity_polling(skip_pending=True)
