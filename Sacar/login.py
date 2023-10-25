from user_base import users

def login(username, password):
    for user in users:
        if username == user['username'] and password == user['password']:
            return True
    return False    