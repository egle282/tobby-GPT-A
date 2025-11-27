import json

def check_subscription(user_id):
    try:
        with open('data/subscribers.json', encoding='utf-8') as f:
            subs = json.load(f)
        return str(user_id) in subs
    except Exception:
        return False
