cost = f"\nTo calculate the cost of the ticket, please indicate your income."
cost += f"\nPlease enter your age: "

while True:
    age_input = input(cost)
    if age_input == 'quit':
        break
    age = int(age_input)

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15


    print(f"The cost your ticket {price}$"
          f"\nIf you no longer require a ticket, please enter 'quit': ")
