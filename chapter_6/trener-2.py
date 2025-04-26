# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)
from chapter_6.trener import favorite_languages

# # aliens = []
# создаём 30 пришельцев, передаём им атрибуты и сохраняем в списке
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# превразаем первых трёх зелёных пришельцев в жёлтых
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# # вывод первых 5 пришельцев
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# print(f"Total number of aliens: {len(aliens)}")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       f"with thee following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
#
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}\'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}"
          f"\tLocation: {location.title()}")
