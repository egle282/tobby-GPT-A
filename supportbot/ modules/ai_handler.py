python
import openai

class AIHandler:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        openai.api_key = "ВАШ_OPENAI_API_KEY"

    def handle(self, msg):
        if not self.feature_on('ai_handler'): return False
        if not msg.text: return False
        # Простейшая интеграция с ChatGPT
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты бот-помощник поддержки"},
                    {"role": "user", "content": msg.text},
                ],
                max_tokens=128
            )
            answer = resp["choices"][0]["message"]["content"]
            self.bot.send_message(msg.chat.id, answer)
            return True
        except Exception as e:
            print(e)
            return False
``
