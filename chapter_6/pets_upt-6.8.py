bullet = {
    'owners name': 'john',
    'breed': 'cane corso',
}
rex = {
    'owners name': 'victor',
    'breed': 'german shepherd'
}
bubble = {
    'owners name': 'eric',
    'breed': 'husky'
}
pets = [bullet, rex, bubble]
for pet in pets:
    pet_info = (f"Owner: {pet['owners name'].title()} "
                f"\n\tAnimal breed: {pet['breed'].title()}")
    print(f"\t{pet_info}")