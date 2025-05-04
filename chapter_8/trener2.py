# def make_pizza(*toppings):
#     print(toppings)
# make_pizza('peperoni')
# make_pizza('mushrooms', 'extra cheese', 'green peppers')

# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-centimeters pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping.title()}")
# make_pizza(27, 'peperoni')
# make_pizza(40, 'mushrooms', 'extra cheese', 'green peppers')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile(
    'albert', 'einstein',
          location='princeton',
          field='physics',
)
print(user_profile)
