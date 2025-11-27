from config import BOT_TOKEN
import telebot

# Создай экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

# Важно: все хендлеры импортируются после создания bot!
import handlers.menu
import handlers.qr
import handlers.news
import handlers.faq
import handlers.voice
import handlers.email
import handlers.donate

# Подключаем новые обработчики:
import handlers.common_features   # здесь /start, /help, бесплатные команды
import handlers.premium_features # здесь премиальные/лимитные команды

if __name__ == '__main__':
    bot.infinity_polling()
