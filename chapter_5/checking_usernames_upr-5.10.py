current_users = ['admin', 'john', 'valentin', 'daniel', 'edvard', 'michael']
new_users = list(current_users)
current_users.append('enrique')
new_users.append('Enrique')

for new_user in new_users:
    if new_user == current_users:
        print(f'Name {new_user} added.')
    else:
        print(f'The name {new_user} has already been used. Please choose another name')
