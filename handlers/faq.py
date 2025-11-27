from bot import bot
from utils.keyboards import kb_main

@bot.message_handler(commands=['faq'])
@bot.message_handler(func=lambda msg: msg.text == "FAQ")
def handle_faq(msg):
    bot.send_message(msg.chat.id, "Введите свой вопрос или выберите из популярных (реализуйте через FAQ-модуль).", reply_markup=kb_main())
    # Можно подключить свой модуль FAQ; пример:
    # answer = faq_search.handle_question(msg.text)
    # bot.send_message(msg.chat.id, answer, reply_markup=kb_main())
