print("Для выхода нажмите 'q'")

while True:
    number1 = (input("\nВведите первое число: "))
    if number1 == 'q':
        break
    number2 = (input("\nВведите второе число: "))
    if number2 == 'q':
        break
    try:
        result = int(number1) + int(number2)
    except ValueError:
        print("Нужно ввести число")
    else:
        print(result)

