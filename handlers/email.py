from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main

@bot.message_handler(func=lambda msg: msg.text == "Отправить Email")
def handle_email(msg):
    bot.send_message(msg.chat.id, "Напишите email-текст", reply_markup=kb_main())
    set_state(msg.from_user.id, "wait_email_input")
# И обработку текстов для email
