topping = f"\nWould you like to add topping to your pizza?"
topping += f"\n(If you don't want to enter 'quit'): "
while True:
    toppings = input(topping)
    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} included in the order!")