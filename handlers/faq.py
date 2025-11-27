from bot import bot
from utils.keyboards import kb_main

@bot.message_handler(func=lambda msg: msg.text == "FAQ")
def handle_faq(msg):
    bot.send_message(msg.chat.id, "Введи вопрос или выбери из популярных.", reply_markup=kb_main())
    # Тут твоя логика
