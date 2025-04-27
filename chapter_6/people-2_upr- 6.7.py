person1 = {
    'first_name': 'james',
    'last_name': 'bond',
    'age': 45,
    'city': 'london',
}
person2 = {
    'first_name': 'steven',
    'last_name': 'seagal',
    'age': 52,
    'city': 'america',
}
person3 = {
    'first_name': 'joe',
    'last_name': 'black',
    'age': 29,
    'city': 'america',
}
peoples = [person1, person2, person3,]
for people in peoples:
    full_name = f"{people['first_name']} {people['last_name']}"
    location = people['city']
    print(f"\n\tFull name: {full_name.title()}"
          f"\n\tLocation: {location.title()}")