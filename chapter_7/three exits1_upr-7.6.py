coast = f"\nTo calculate the cost of the ticket, please indicate your income."
coast += f"\nPlease enter your age: "
active = True
while active:
    age = int(input(coast))
    if age == 'quit':
        active = False
    else:
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15
        print(f"The cost your ticket {price}$"
              f"\nIf you no longer require a ticket, please enter 'quit': ")
