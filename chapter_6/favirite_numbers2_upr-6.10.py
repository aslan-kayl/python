favorite_numbers = {
    'john': [4, 23],
    'victor': [67, 12],
    'logan': [10, 4],
    'eric': [12, 53],
    'charley': [14, 44],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}\'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
