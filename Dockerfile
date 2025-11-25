Dockerfile
FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y libzbar0 ffmpeg

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
