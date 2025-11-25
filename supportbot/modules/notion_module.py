```python
"""
notion_module.py
----------------
Пример дополнительного модуля интеграции с Notion API:
Отправляет все обращения в специальную базу уведомлений.
Для работы нужен сервисный токен, id базы (БД) в Notion.
"""
import os
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
NOTION_DB = os.getenv("NOTION_DB", "")

class NotionModule:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def push_to_notion(self, text, username):
        if not NOTION_TOKEN or not NOTION_DB:
            return False
        url = "https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "parent": {"database_id": NOTION_DB},
            "properties": {
                "Title": {"title": [{"text": {"content": text[:200]}}]},
                "User": {"rich_text": [{"text": {"content": username}}]}
            }
        }
        r = requests.post(url, headers=headers, json=data)
        return r.status_code == 200 or r.status_code == 201
      def handle(self, msg):
        if not self.feature_on('notion_module'):
            return False
        # Можно сделать любое условие, пример: все сообщения длиннее 15 символов
        if msg.text and len(msg.text.strip()) > 15:
            self.push_to_notion(msg.text, str(msg.from_user.id))
            self.bot.send_message(msg.chat.id, "Ваш вопрос отправлен. Спасибо!")
            return True
        return False
``
