python
import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or "ВАШ_ТОКЕН"
ADMIN_IDS = [int(uid) for uid in os.getenv("ADMIN_IDS", "ваш_ID_админа").split(",")]

DATA_PATH = 'data/'
FAQ_FILE = DATA_PATH + 'faq.json'
HISTORY_FILE = DATA_PATH + 'user_history.json'
