# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print(f"Verifying user: {current_users.title()}")
#     confirmed_users.append(current_users)
# print(f"\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'rabbit', 'cat', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# for pet in pets:
#     print(pet)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? : ")
    response = input("\nWhich mountain would you like to climb someday? : ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) : ")
    if repeat == 'no':
        polling_active = False
print("\n       ----Roll Results----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")