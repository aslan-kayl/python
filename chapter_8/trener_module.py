def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-centimeters pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")