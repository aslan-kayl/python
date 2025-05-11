import json


filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:

    favorite_number = int(input("Введите любимое число: "))
    my_number = 'favorite_number.json'

    with open(my_number, 'w') as f:
        json.dump(favorite_number, f)
    print(f"Я знаю ваше любимое число это: {favorite_number}")
else:
    print("Ваше число уже соханено")
