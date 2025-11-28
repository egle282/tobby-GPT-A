from loader import bot

# Импорт всех хендлеров, как в bot.py
import handlers.menu
import handlers.qr
import handlers.news
import handlers.faq
import handlers.voice
import handlers.email
import handlers.donate
import handlers.common_features
import handlers.premium_features

from flask import Flask, request
import telebot
import os

app = Flask(__name__)

# Для healthcheck (Render требует)
@app.route('/', methods=['GET'])
def index():
    return 'OK', 200

# Основной webhook endpoint
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Invalid request!', 400

if __name__ == '__main__':
    # Подгрузи WEBHOOK из config.py или явно пропиши здесь
    WEBHOOK_URL = "https://helpinos-gpt-a.onrender.com/"
    bot.remove_webhook()
    bot.set_webhook(WEBHOOK_URL)
    # Render предусматривает переменную PORT!
    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)
