rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yenisei': 'russia',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers:
    print(river.title())
for country in rivers.values():
    print(country.title())