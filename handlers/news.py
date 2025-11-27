from bot import bot
from utils.states import set_state, get_state, clear_state
from utils.keyboards import kb_main, kb_location
from config import NEWS_API_KEY
import requests

def get_city_from_location(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {'format': 'json', 'lat': lat, 'lon': lon, 'zoom': 10, 'addressdetails': 1}
    try:
        resp = requests.get(url, params=params, timeout=10)
        address = resp.json().get("address", {})
        city = address.get("city") or address.get("town") or address.get("village") or address.get("state")
        country = address.get("country_code")
        return city, country
    except Exception:
        return None, None

def get_news_by_city(city, country=None, api_key=None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "q": city,
        "pageSize": 5,
        "language": "ru" if country=="ru" else "en",
    }
    try:
        data = requests.get(url, params=params, timeout=10).json()
        if data.get("status") != "ok":
            return []
        return [f"{a['title']}\n{a['url']}" for a in data.get("articles", [])]
    except Exception:
        return []

@bot.message_handler(func=lambda msg: msg.text == "📢 Новости")
def news_start(msg):
    bot.send_message(msg.chat.id, "Пожалуйста, отправьте свою геолокацию или выберите:", reply_markup=kb_location())
    set_state(msg.from_user.id, "wait_location")

@bot.message_handler(content_types=['location'])
def handle_location(msg):
    if get_state(msg.from_user.id) == "wait_location":
        lat, lon = msg.location.latitude, msg.location.longitude
        city, country = get_city_from_location(lat, lon)
        if not city:
            bot.send_message(msg.chat.id, "Не удалось определить город. Введите его вручную.")
            set_state(msg.from_user.id, "wait_manual_city")
            return
        bot.send_message(msg.chat.id, f"Определён город: {city}")
        news = get_news_by_city(city, country, NEWS_API_KEY)
        reply = "\n\n".join(news) if news else "Новостей для этого города нет."
        bot.send_message(msg.chat.id, reply, reply_markup=kb_main())
        clear_state(msg.from_user.id)
@bot.message_handler(func=lambda msg: get_state(msg.from_user.id) == "wait_manual_city")
def handle_city(msg):
    news = get_news_by_city(msg.text, api_key=NEWS_API_KEY)
    reply = "\n\n".join(news) if news else "Новостей для этого города нет."
    bot.send_message(msg.chat.id, reply, reply_markup=kb_main())
    clear_state(msg.from_user.id)
