states = {}

def set_state(user_id, state):
    states[user_id] = state

def get_state(user_id):
    return states.get(user_id)

def clear_state(user_id):
    states.pop(user_id, None)
