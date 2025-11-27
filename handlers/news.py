from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main
@bot.message_handler(func=lambda msg: msg.text == "📢 Новости")
def news_start(msg):
    bot.send_message(msg.chat.id, "Функция новостей!") # Вставь свою логику
