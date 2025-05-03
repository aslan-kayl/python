coast = f"\nPlease enter your age: "
while True:
    age = int(input(coast))
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"The cost your ticket {price}$")
    