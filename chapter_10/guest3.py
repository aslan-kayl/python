def get_answer():
    run = True
    while True:
        name_input = input("Введите своё имя : ")
        print(f"Добро пожаловать {name_input.title()}")

        guest = 'my_guest.txt'
        with open(guest, 'w') as file_object:
            file_object.write(f"Меня зовут {name_input}\n")

        my_way_programming = input('Почему вам нравится программировать? : ')
        # print(f"{my_way_programming.title()}")
        answer = 'my_guest.txt'
        with open(answer, "a") as file_object:
                 file_object.write(f'\tМне нравится программировать потому что - {my_way_programming}')
        break
# get_answer()

def add_data():
    run = True
    while True:
        name_input = input("Введите своё имя : ")
        print(f"Добро пожаловать {name_input.title()}")

        guest = 'my_guest.txt'
        with open(guest, 'a') as file_object:
            file_object.write(f"\nМеня зовут {name_input}\n")

        my_way_programming = input('Почему вам нравится программировать? : ')
        # print(f"{my_way_programming.title()}")
        answer = 'my_guest.txt'
        with open(answer, "a") as file_object:
                 file_object.write(f'\tМне нравится программировать потому что - {my_way_programming}')
        break

add_data()