python
import openai
import os

class AIHandler:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        openai.api_key = os.getenv('OPENAI_API_KEY', '')

    def handle(self, msg):
        if not self.feature_on('ai_handler'):
            return False
        text = (msg.text or '').strip()
        if not text: return False
        # Обрабатываем только не-FAQ и не-односложные вопросы (>10 слов)
        if len(text.split()) < 10: return False
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты умный ассистент поддержки."},
                    {"role": "user", "content": text},
                ],
                max_tokens=100
            )
            answer = resp["choices"][0]["message"]["content"]
            self.bot.send_message(msg.chat.id, f"🤖 AI-подсказка:\n{answer}")
            return True
        except Exception as e:
            print(e)
            return False
```
