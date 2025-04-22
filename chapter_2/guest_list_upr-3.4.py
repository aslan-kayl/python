guest = ['Roberto', 'Enrique', 'Juan']
# print(f"\nHi {guest[0]}, there's a dinner party tonight at 7, I'd be glad if you came."
#       f"\nHi {guest[1]}, there's a dinner party tonight at 7, I'd be glad if you came."
#       f"\nHi {guest[2]}, there's a dinner party tonight at 7, I'd be glad if you came.")
# delete_g = guest.pop(2)
# guest.append('Alvaro')
# print(f"\nHi {guest[0]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
#       f"\nHi {guest[1]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
#       f"\nHi {guest[2]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came.")
# print(delete_g)

guest.insert(0, 'Paolo')
guest.insert(2, 'Alberto')
guest.append('Antonio')
print(f"\nHi {guest[0]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
      f"\nHi {guest[1]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
      f"\nHi {guest[2]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
      f"\nHi {guest[3]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
      f"\nHi {guest[4]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came."
      f"\nHi {guest[5]}, me hermano there's a dinner party tonight at 7, I'd be glad if you came.")
print(guest)

delete_g = guest.pop(), guest.pop(), guest.pop(), guest.pop()
print(f'\nDear {delete_g[0]}, I\'m very sorry but I can\'t have you over today.'
      f'\nDear {delete_g[1]}, I\'m very sorry but I can\'t have you over today.'
      f'\nDear {delete_g[2]}, I\'m very sorry but I can\'t have you over today.'
      f'\nDear {delete_g[3]}, I\'m very sorry but I can\'t have you over today.'
      f'\nDear {guest[0]}, my invitation is still valid, I\'m waiting for you to visit.'
      f'\nDear {guest[1]}, my invitation is still valid, I\'m waiting for you to visit.')
del guest[0]
del guest[1]
print(guest)