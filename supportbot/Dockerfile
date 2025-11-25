Dockerfile
# Была проблема с Pillow 12+ на slim, для стабильной работы возьмём основной python
FROM python:3.10

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем все остальные файлы бота
COPY . .

# Для pyzbar нужны system-библиотеки (zbar)
RUN apt-get update && apt-get install -y libzbar0

# Стартуем основной скрипт
CMD ["python", "bot.py"]
