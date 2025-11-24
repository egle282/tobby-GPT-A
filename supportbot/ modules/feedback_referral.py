python
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class FeedbackReferral:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        if not self.feature_on('feedback_referral'):
            return False
        if msg.text and 'оцен' in msg.text.lower():
            kb = InlineKeyboardMarkup()
            for i in range(1, 6):
                kb.add(InlineKeyboardButton(f'⭐️{i}', callback_data=f'fb_{i}'))
            kb.add(InlineKeyboardButton('🔗 Пригласить друга', switch_inline_query=''))
            self.bot.send_message(msg.chat.id, "Как вы оцениваете нашу работу?", reply_markup=kb)
            return True
        return False

# В основном файле (bot.py) добавьте:
# @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('fb_'))
# def handle_feedback(call):
#     stars = call.data[3:]
#     bot.answer_callback_query(call.id, f"Спасибо за {stars}⭐️!")
#     bot.send_message(call.from_user.id, "Спасибо за вашу оценку!")
```
