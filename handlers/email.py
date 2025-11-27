from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main
from modules.send_email import SendEmail
from config import ADMIN_EMAIL

send_email_module = SendEmail(bot, lambda name: True, ADMIN_EMAIL)  # Разреши по желанию
@bot.message_handler(func=lambda msg: msg.text == "Отправить Email")
def email_start(msg):
    bot.send_message(msg.chat.id, "Введите сообщение для Email:")
    set_state(msg.from_user.id, "wait_email_input")

@bot.message_handler(func=lambda msg: get_state(msg.from_user.id) == "wait_email_input")
def email_handle(msg):
    if hasattr(send_email_module, "handle"):
        send_email_module.handle(msg, msg.text)
        bot.send_message(msg.chat.id, "Ваш Email отправлен.", reply_markup=kb_main())
    else:
        bot.send_message(msg.chat.id, "Ошибка отправки Email.", reply_markup=kb_main())
    clear_state(msg.from_user.id)
