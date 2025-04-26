favorite_languages = {
    'phil': 'c',
    'sarah': 'c#',
    'edvard': 'python',
    'jen': 'java script',
    'robert': 'c',
}

new_people = ['chris', 'newman', 'jen', 'robert',]
for name in new_people:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for participating")
    else:
        print(f"{name.title()}, would you like to take the survey?")
