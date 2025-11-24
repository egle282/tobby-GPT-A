python
import os

# Ваш токен бота Telegram (или добавьте в Render/env)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_ЗДЕСЬ")

# ID администраторов (через запятую)
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "123456789").split(",") if x.strip().isdigit()]

DATA_PATH = 'data/'
FAQ_FILE = DATA_PATH + 'faq.json'
HISTORY_FILE = DATA_PATH + 'user_history.json'

# OpenAI API ключ для AI-ответов (в env OPENAI_API_KEY)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
