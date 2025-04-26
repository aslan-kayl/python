# cars = ['audi', 'bmw', 'toyota', 'suzuki', 'subaru']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

#cars = 'AUDI'
# if cars.lower() == 'audi':
#     print(cars)

# age1 = 18
# age2 = 21
# if age1 == 20 and age2 == 21:
#     print('good!!!')
# else:
#     print('bad!!!')

# toppings = ['mushrooms', 'onions', 'pineapple']
# my_toppings = 'beef'
# if 'beef' not in toppings:
#     print(f'topping {my_toppings.title()}, is not in list')

# age = 61
# if age < 4:
#     print("admission is free")
# elif age < 18:
#     print("entrance fee is 25 dollars")
# elif age > 60:
#     print("admission is free")
# else:
#     print("entrance fee is 40 dollars")

# age = 22
# if age < 4:
#     price = 0
# elif age <18:
#     price = 25
# else:
#     price = 40
# print(f'Your admission cost to ${price}.')

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers right now.')
#     else:
#         print(f'Adding {requested_topping}.')
# print("\nFinished making your pizza!")

# requested_toppings = ['extra cheese',]
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if requested_topping == 'green pepper':
#             print("Sorry, we are out of green peppers right now.")
#         else:
#             print(f'Adding {requested_topping}.')
# else:
#     print(f"Are you sure you want a plain pizza?")

available_toppings = [
    'mushrooms',
    'olives',
    'green peppers',
    'pepperoni',
    'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry we don\'t have {requested_topping}.')
print("\nFinished making your pizza!")