def get_answer():
    run = True
    while run:
        name_input = input("Для выхода введите 'quit' "
                           "\nПожалуйста введите свое имя : ")
        if name_input == 'quit':
            run = False
        else:
            print(f"Добро пожаловать {name_input.title()}")
            guest = 'my_guest.txt'
            with open(guest, 'a') as file_object:
                file_object.write(f"{name_input}\n")

get_answer()