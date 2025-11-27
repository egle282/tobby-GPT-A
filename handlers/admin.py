from telebot import types
from utils.subscription import add_subscriber, remove_subscriber
from config import ADMINS

@bot.message_handler(commands=['add_subscriber'])
def admin_add_sub(msg):
    if msg.from_user.id not in ADMINS:
        bot.send_message(msg.chat.id, "Нет прав.")
        return
    try:
        user_id = int(msg.text.split()[1])
        add_subscriber(user_id)
        bot.send_message(msg.chat.id, f"Пользователь {user_id} теперь подписчик.")
    except Exception:
        bot.send_message(msg.chat.id, "Ошибка. Используй /add_subscriber user_id")

@bot.message_handler(commands=['remove_subscriber'])
def admin_remove_sub(msg):
    if msg.from_user.id not in ADMINS:
        bot.send_message(msg.chat.id, "Нет прав.")
        return
    try:
        user_id = int(msg.text.split()[1])
        remove_subscriber(user_id)
        bot.send_message(msg.chat.id, f"Пользователь {user_id} удалён из подписчиков.")
    except Exception:
        bot.send_message(msg.chat.id, "Ошибка. Используй /remove_subscriber user_id")
