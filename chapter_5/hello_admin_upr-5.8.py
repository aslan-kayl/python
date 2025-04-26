# names = ['admin', 'john', 'valentin', 'daniel', 'edvard', 'michael']
# for name in names:
#     if name == 'admin':
#         print(f'Hello Admin, would you like to see a status report?')
#     else:
#         print(f'Helo {name.title()}, thank you for logging in again.')

names = ['admin ']
if names:
    for name in names:
        if name == 'admin':
            print(f'Hello Admin, would you like to see a status report?')
        else:
            print(f'Helo {name.title()}, thank you for logging in again.')
else:
    print("We need ti ind some users!")