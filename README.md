markdown
# SupportBot Pro
Универсальный Telegram-бот поддержки со сменными модулями: FAQ, AI, файлы, уведомления, мультиязык, рассылка новостей, QR-сканер, рефералы и автоответы.
## Быстрый старт
1. Клонируйте репозиторий:
2.   git clone https://github.com/your/repo.git
     cd helpino-bot
3. Установите зависимости:
   pip install -r requirements.txt
4. Скопируйте файлы в папки modules/ и data/.
5. Создайте переменные окружения:  
   - BOT_TOKEN, ADMIN_IDS, OPENAI_API_KEY  
   (или отредактируйте в config.py)
6. Запуск:  
   python bot.py
7.  (Опционально, если используете Docker)
   docker build -t helpino .
   docker run -e BOT_TOKEN=ваш_токен --rm helpino

## Модули

- **context_support** — хранение истории сообщений
- **file_module** — загрузка и пересылка файлов/фото
- **multilang** — мультиязычие и авто-перевод
- **personalized** — персональные автоответы
- **feedback_referral** — сбор отзывов и реферальные ссылки
- **faq_search** — интеллектуальный поиск по FAQ
- **qr_scanner** — распознает коды с изображений
- **push_notify** — push и рассылка уведомлений
- **cross_platform** — переадресация в VK, WhatsApp и т.д.
- **mailing** — подписка и новостные рассылки
- **ai_handler** — AI-обработка сложных вопросов
- 
## Описание структуры
- `bot.py`           — стартовый скрипт.
- `handlers/`        — логика команд Telegram.
- `modules/`         — отдельные модули логики (FAQ, QR, почта...).
- `utils/`           — вспомогательные утилиты (состояния, клавиатуры).
- `data/`            — хранение статичных и рабочих JSON (faq.json, user_history.json).
- `requirements.txt` — Python-зависимости.
- `apt.txt`          — системные пакеты для сборки контейнера.
- `generate_stubs.py`— инициализация пустых файлов данных.
- `Dockerfile`       — контейнеризация.

## Настройка переменных
- BOT_TOKEN         — токен Telegram-бота
- WEBHOOK_URL       — URL вебхука (если используется)
- PORT              — порт для webhook (по умолчанию 8443)

Все переменные можно задавать через environment или `.env`-файл (если добавите поддержку через python-dotenv).

## Запуск отдельной генерации данных
bash
python generate_stubs.py

## Для админов
- Активация/деактивация модулей:
  /admin_toggle <module> on|off`
## Лицензия
MIT (или ваша)
