```python
import os
import telebot
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Импорт основных модулей
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

# Интеграции
from modules.mail_inbox import MailInbox
from modules.send_email import SendEmail
from modules.voice_module import VoiceModule
from modules.custom_filters import CustomFilters

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
    "mail_inbox": True,
    "send_email": True,
    "voice_module": True,
    "custom_filters": True,
}

def feature_on(name): return modules_enabled.get(name, False)

# Инициализация
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
mail_inbox = MailInbox(bot, feature_on)
send_email = SendEmail(bot, feature_on)
voice_module = VoiceModule(bot, feature_on)
custom_filters = CustomFilters(bot, feature_on)

def gen_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛈 FAQ", "💬 Поддержка")
    kb.add("📎 Файл", "📷 QR-сканер")
    kb.add("📢 Новости", "🎤 Голосовое")
    kb.add("Оценить", "Отправить Email")
    return kb

@bot.message_handler(commands=['start'])
def handle_start(msg):
    bot.send_message(
        msg.chat.id,
        f'Привет! Я Helpino — бот поддержки. Выберите действие или задайте вопрос:',
        reply_markup=gen_menu()
    )

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
        bot.send_message(msg.chat.id, f"Модуль `{mod}` теперь {'включен' if state == 'on' else 'выключен'}")
    except Exception:
        bot.send_message(msg.chat.id, "Формат: /admin_toggle module on/off")

@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('fb_'))
def handle_feedback(call):
    stars = call.data[3:]
    bot.answer_callback_query(call.id, f"Спасибо за {stars}⭐️!")
    bot.send_message(call.from_user.id, "Спасибо за вашу оценку!")
    @bot.message_handler(content_types=['text', 'voice', 'photo', 'document'])
def router(msg):
    # Фильтры и голосовые всегда выше всего!
    if custom_filters.handle(msg): return
    if voice_module.handle(msg): return
    # ядро + интеграции дальше
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
    if send_email.handle(msg): return
    bot.send_message(msg.chat.id, "Ваш запрос передан в поддержку — выберите задачу из меню для ускорения.")

import threading, time

def mail_loop():
    while True:
        try:
            mail_inbox.check_mail()
        except Exception as ex:
            print(f"Mail check error: {ex}")
        time.sleep(60)

# WEBHOOK MODE FOR CLOUD (RENDER, etc.)
if __name__ == '__main__':
    if WEBHOOK_URL:
        bot.remove_webhook()
        bot.set_webhook(url=WEBHOOK_URL)
        from flask import Flask, request

        app = Flask(__name__)

        @app.route('/', methods=['POST'])
        def receive_update():
            if request.headers.get('content-type') == 'application/json':
                bot.process_new_updates([telebot.types.Update.de_json(request.data.decode("utf-8"))])
                return '', 200
            return '', 403

        @app.route('/', methods=['GET'])
        def alive():
            return "Helpino bot working!", 200

        threading.Thread(target=mail_loop, daemon=True).start()
        app.run(host='0.0.0.0', port=PORT, debug=False)
    else:
        threading.Thread(target=mail_loop, daemon=True).start()
        bot.infinity_polling(skip_pending=True)
