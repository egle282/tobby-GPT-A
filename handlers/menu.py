from bot import bot
from utils.keyboards import kb_main

@bot.message_handler(commands=['start'])
def handle_start(msg):
    bot.send_message(
        msg.chat.id,
        "Привет! Я Helpino — бот поддержки. Выберите действие или задайте вопрос:",
        reply_markup=kb_main()
    )

@bot.message_handler(commands=['donate'])
def handle_donate(msg):
    bot.send_message(msg.chat.id, "Спасибо за интерес к поддержке!")
    bot.send_message(msg.chat.id, "Главное меню:", reply_markup=kb_main())

@bot.message_handler(func=lambda msg: msg.text == "Главное меню")
def handle_main_menu(msg):
    bot.send_message(msg.chat.id, "Главное меню:", reply_markup=kb_main())
