# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f'You just earned {new_points} points!')

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# # print(alien_0 )
# alien_0['color'] = 'yellow'
# print(alien_0)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print(f"Original position: {alien_0['x_position']}")
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# del alien_0['color']
# print(alien_0)

# alien_0 = {'color': 'green', 'speed': 'slow',}
# point_value = alien_0.get('points', '')
# print(point_value )

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(key, ':', value)

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edvard': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_language.items():
#     print(f'{name.title()}\' favorite language is {language.title()}')

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edvard': 'ruby',
#     'phil': 'python',
# }
#
# for name in favorite_language:
#     print(name.title())

# favorite_languages = {
#     'phil': 'c',
#     'sarah': 'python',
#     'edvard': 'python',
#     'jen': 'c',
#     'robert': 'jawa',
# }
# friends = ['phil', 'sarah',]
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}!")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you lobe {language.title()}!")

# favorite_languages = {
#     'phil': 'c',
#     'sarah': 'python',
#     'edvard': 'python',
#     'jen': 'c',
#     'robert': 'jawa',
# }
# if 'iren' not in favorite_languages:
#     print("Erin, please take our poll!")

# favorite_languages = {
#     'phil': 'c',
#     'sarah': 'python',
#     'edvard': 'python',
#     'jen': 'c',
#     'robert': 'jawa',
# }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# favorite_languages = {
#     'phil': 'c',
#     'sarah': 'c#',
#     'edvard': 'python',
#     'jen': 'java script',
#     'robert': 'java',
# }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# favorite_languages = {
#     'phil': 'c',
#     'sarah': 'c#',
#     'edvard': 'python',
#     'jen': 'java script',
#     'robert': 'c',
# }
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

favorite_languages = {'c', 'c#', 'python', 'java script', 'c',}
for language in favorite_languages:
    print(language)