import json

def get_stored_username():
    filename = 'my_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Введите своё имя: ")
    filename = 'my_username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    while True:
        username = get_stored_username()
        print(username)
        check = input("Is the user name correctly defined? (yes/no): ")
        if check == 'yes' or check == 'y':
            print(f"Welcome back {username}! ")
            break
        else:
            username = get_new_username()
            print(f"Your name {username} is added to the list")
            break
greet_user()