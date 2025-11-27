from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main

@bot.message_handler(func=lambda msg: msg.text == "🎤 Голосовое")
def handle_voice(msg):
    bot.send_message(msg.chat.id, "Отправьте голосовое или текст", reply_markup=kb_main())
    set_state(msg.from_user.id, "wait_voice")
# Добавь остальную обработку по аналогии
