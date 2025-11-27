states = {}

def set_state(user, value):
    states[user] = value

def get_state(user):
    return states.get(user)

def clear_state(user):
    states.pop(user, None)
