import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(u) for u in os.getenv("ADMIN_IDS", "123456789").split(",")]
DATA_PATH = 'data/'
FAQ_FILE = f"{DATA_PATH}faq.json"
HISTORY_FILE = f"{DATA_PATH}user_history.json"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 5000))

# Почта IMAP и SMTP
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASS = os.getenv("IMAP_PASS")
IMAP_FOLDER = os.getenv("IMAP_FOLDER", "INBOX")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
