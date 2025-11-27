from config import BOT_TOKEN
import telebot

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

# Инициализация всех хендлеров (ВАЖНО: импортировать после создания bot!)
import handlers.menu
import handlers.qr
import handlers.news
import handlers.faq
import handlers.voice
import handlers.email

if __name__ == '__main__':
    bot.infinity_polling()
