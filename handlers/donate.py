from bot import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['donate'])
@bot.message_handler(func=lambda m: m.text and m.text.lower() == "донат")
def handle_donate(msg):
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton("Boosty", url="https://boosty.to/yourpage"))
    kb.row(InlineKeyboardButton("TON (TON Space)", url="https://t.me/yourTONlink"))
    # Можешь добавить свои платежные ссылки ниже
    
    bot.send_message(
        msg.chat.id,
        "Спасибо за желание поддержать проект! Ваша поддержка помогает развитию бота. "
        "Выберите удобный для вас способ оплаты ниже 👇\n\n"
        "Я не являюсь ИП/ООО, поддержка производится как добровольное пожертвование.\n"
        "Если оплатили — буду рад вашему сообщению! 😊",
        reply_markup=kb)
    bot.send_message(
        msg.chat.id,
        "Если удобнее — можете поддержать по номеру карты: 2202 xxxx xxxx 0000\n"
        "ИЛИ по ЮMoney: 4100xxxxxxxxxxx\n"
        "(укажите свой ник в боте, чтобы я мог сказать спасибо!)"
    )
