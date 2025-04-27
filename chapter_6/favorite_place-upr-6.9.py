favorite_places = {
    'aslan': {
    'place1': 'alberobello',
    'place2': 'granada',
    'place3': 'melaka',
    },
    'kayl': {
    'place1': 'Fairbanks',
    'place2': 'aphens',
        'place3': 'london',
    },
    'nikolas': {
        'place1': 'mexico',
        'place2': 'lisabon',
        'place3': 'manila',
    },
}
for username, user_info in favorite_places.items():
    print(f'Username: \n\t{username.title()}')
    for place in user_info.items():
        places = (
            f"\n\t{user_info['place1']}\n"
            f"\t{user_info['place2']}\n"
            f"\t{user_info['place3']}\n"
        )
    print(f"Favorite places: {places.title()}")

