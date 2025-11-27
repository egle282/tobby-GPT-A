from loader import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main
from modules.voice_module import VoiceModule
from modules.ai_handler import AIHandler

voice_module = VoiceModule(bot)
ai_handler = AIHandler(bot)

@bot.message_handler(func=lambda msg: msg.text == "🎤 Голосовое")
def handle_voice_start(msg):
    bot.send_message(msg.chat.id, "Пожалуйста, отправьте голосовое сообщение.")
    set_state(msg.from_user.id, "wait_voice")

@bot.message_handler(content_types=['voice'])
def handle_voice(msg):
    if get_state(msg.from_user.id) == "wait_voice":
        text = voice_module.handle(msg) # Разреши в modules/voice_module.py и верни текст
        if not text:
            bot.send_message(msg.chat.id, "Ошибка распознавания речи.", reply_markup=kb_main())
            clear_state(msg.from_user.id)
            return
        bot.send_message(msg.chat.id, f"Распознано: {text}\n\nВведите язык для перевода (ru, en, de):")
        set_state(msg.from_user.id, ("wait_voice_translate", text))

@bot.message_handler(func=lambda msg: isinstance(get_state(msg.from_user.id), tuple) and get_state(msg.from_user.id)[0] == "wait_voice_translate")
def handle_translate(msg):
    text = get_state(msg.from_user.id)[1]
    lang = msg.text.strip().lower()
    translated = ai_handler.translate(text, lang)
    bot.send_message(msg.chat.id, f"Перевод:\n{translated}", reply_markup=kb_main())
    bot.send_message(msg.chat.id, "Хотите получить голосовой ответ? Пока функция отсутствует (заглушка).", reply_markup=kb_main())
    clear_state(msg.from_user.id)
