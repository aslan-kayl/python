def get_answer():
    run = True
    while run:
        name_input = input("Для того что бы завершить опрос введите 'quit' "
                           "\nВведите свое имя : ")
        if name_input == 'quit':
            run = False
        else:
            guest = 'my_guest.txt'
            with open(guest, 'w') as file_object:
                file_object.write(name_input)

get_answer()