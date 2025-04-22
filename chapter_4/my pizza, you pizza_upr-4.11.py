my_favorite_pizzas = ['peperoni', '4 cheeses', 'margarita']
friend_pizzas = my_favorite_pizzas[:]
my_favorite_pizzas.append('with gorgonzola')
friend_pizzas.append('with roastbeef')
print("My favorite pizzas are:")
for value in my_favorite_pizzas:
    print(value)
print('\nMy friend\'s favorite pizzas are:')
for value in friend_pizzas:
    print(value)