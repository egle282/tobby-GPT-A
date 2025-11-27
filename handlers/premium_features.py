from telebot import TeleBot
from utils.limits import can_use_feature, add_user_action

from loader import bot
@bot.message_handler(commands=['...'])
def func(...):

# =========================
# 1. Голосовое распознавание
# =========================
@bot.message_handler(commands=['voice'])
def handle_voice(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'voice'):
        bot.send_message(
            msg.chat.id,
            "🔒 Голосовое распознавание: только 3 раза в сутки бесплатно. Купите подписку для безлимитного доступа!"
        )
        return

    # --- Твой код голосового распознавания ---
    # resp_text = распознать_голос(msg)  # <- вставь здесь свою функцию

    add_user_action(user_id, 'voice')
    bot.send_message(msg.chat.id, "Ваше голосовое сообщение успешно распознано! ✅")


# ===============================================
# 2. Формирование PDF/отправка на e-mail через бота
# ===============================================
@bot.message_handler(commands=['pdf'])
def handle_pdf(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'pdf'):
        bot.send_message(
            msg.chat.id,
            "🔒 Создание PDF/отправка: максимум 5 документов в сутки бесплатно. Оформи подписку!"
        )
        return

    # --- Твой код формирования PDF ---
    # pdf_file = создать_pdf(msg)  # <- твоё действие
    add_user_action(user_id, 'pdf')
    bot.send_message(msg.chat.id, "Ваш PDF успешно создан и отправлен! ✅")


# ================================
# 3. Интеграция с AI-сервисами/LLM
# ================================
@bot.message_handler(commands=['ask'])
def handle_ai(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'llm'):
        bot.send_message(
            msg.chat.id,
            "🔒 AI: только 2 запроса/день бесплатно. Для безлимита нужна подписка."
        )
        return

    # --- Твой код общения с ИИ ---
    # ai_result = query_ai(msg.text)
    add_user_action(user_id, 'llm')
    bot.send_message(msg.chat.id, f"Ответ получен от AI! ✅")


# ===========================================
# 4. Работа с docx/tar/архивами (2 раза/сутки)
# ===========================================
@bot.message_handler(commands=['docx'])
def handle_docx(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'docx'):
        bot.send_message(
            msg.chat.id,
            "🔒 Работа с docx/архивами: только 2 раза в сутки бесплатно. Неограниченно — с подпиской!"
        )
        return
      # --- Код обработки docx/архивов ---
    # result = process_docx(msg)
    add_user_action(user_id, 'docx')
    bot.send_message(msg.chat.id, "Файл docx обработан! ✅")


# ==============================
# 5. Личный кабинет (только премиум)
# ==============================
@bot.message_handler(commands=['cabinet'])
def handle_cabinet(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'cabinet'):
        bot.send_message(
            msg.chat.id,
            "🔒 Личный кабинет доступен только подписчикам!"
        )
        return

    # --- Код показа личного кабинета ---
    # cabinet_info = get_cabinet_info(user_id)
    bot.send_message(msg.chat.id, "Ваш личный кабинет открыт!")


# ===================================
# 6. Особые уведомления ("VIP"/No ADS)
# ===================================
@bot.message_handler(commands=['vip'])
def handle_vip(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'vip_notif'):
        bot.send_message(
            msg.chat.id,
            "🔒 Эта функция доступна только VIP-подписчикам."
        )
        return

    # --- Действие для VIP ---
    bot.send_message(msg.chat.id, "Премиум-уведомление отправлено!")


@bot.message_handler(commands=['noads'])
def handle_noads(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'no_ads'):
        bot.send_message(
            msg.chat.id,
            "🔒 Отключение рекламы доступно только VIP-подписчикам."
        )
        return

    # --- Отключить рекламу для user_id ---
    bot.send_message(msg.chat.id, "Реклама отключена! Спасибо за подписку.")


# ========================
# 7. Премиум-поддержка
# ========================
@bot.message_handler(commands=['support'])
def handle_support(msg):
    user_id = msg.from_user.id
    if not can_use_feature(user_id, 'support'):
        bot.send_message(
            msg.chat.id,
            "🔒 Премиум-поддержка: только 1 вопрос бесплатно в сутки! Неограниченно — по подписке."
        )
        return

    # --- Здесь отправка сообщения поддержке ---
    # support_result = send_support_question(user_id, msg.text)
    add_user_action(user_id, 'support')
    bot.send_message(msg.chat.id, "Ваша заявка отправлена! Ожидайте ответ поддержки.")
