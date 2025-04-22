# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# digits= list(range(1,1000))
# print(digits)
# print(sum(digits))

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print('Here are the first three players on my team:')
# for player in players[:3]:
#     print(player.title())


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.insert(1, 'ice cream')
print(f"My favorite foods are:\n{my_foods}")
print(f"\nMy friend\'s favorite foods are:\n{friend_foods}")
