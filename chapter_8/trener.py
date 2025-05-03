# def greet_user(username):
#     print(f"Helo, {username.title()}!")
# greet_user('kolya')

# def describe_pet(pet_name, animal_type):
# функция с указанием имени и значении
#     print(f"\nI have a {animal_type}."
#           f"\nMy {animal_type}\'s name is {pet_name.title()}")
#
# describe_pet('mike', 'dog')

# def describe_pet(pet_name, animal_type='dog'):
# фунция для вывода без указания значения animal_type
#     print(f"\nI have a {animal_type}."
#           f"\nMy {animal_type}\'s name is {pet_name.title()}")
#
# describe_pet('mike')

# def describe_pet(pet_name, animal_type='dog'):
#     # функция с изменённым значением (по дефолту должен быть animal_type='dog')
#     print(f"\nI have a {animal_type}."
#           f"\nMy {animal_type}\'s name is {pet_name.title()}")
#
# describe_pet('cupper', animal_type='hamster')

# def get_formated_name(f_name, l_name):
#     # возващаем аккуратно отформатированное имя
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()
# musician = get_formated_name('jimi', 'hendrix')
# print(musician)

# def get_format_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_format_name('john', 'lee', 'hooker')
# print(musician)

# def get_format_name(first_name, last_name, middle_name='', ):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_format_name('jimi', 'hendrix')
# print(musician)
# musician = get_format_name('john', 'hooker', 'lee')
# print(musician)

# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def get_formated_name(f_name, l_name):
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name: ")
#     print("enter 'q' at any time to quit")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formated_name = get_formated_name(f_name, l_name)
#     print(f"\nHello, {formated_name}!")

# def greet_users(names):
#     for name in names:
#         msg = f"Hello {name.title()}!"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print(f"\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)