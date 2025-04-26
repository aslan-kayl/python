car = 'subaru'
if car == 'subaru':
    print(True)
else:
    print(False)

car = 'subaru'
if car != 'subaru':
    print(True)
else:
    print(False)

car = 'SUBARU'
if car.lower() == 'subaru':
    print(True)
else:
    print(False)

car = 20
if car == 20:
    print(True)
else:
    print(False)

car = 20
if car <= 20:
    print(True)
else:
    print(False)

car = 20
if car >= 20:
    print(True)
else:
    print(False)

car = 20
if car == 20 and car <= 30:
    print(True)
else:
    print(False)

car = 20
if car == 20 or car <= 10:
    print(True)
else:
    print(False)

car = ['audi', 'bmw', 'honda', 'nissan']
if 'nissan' in car:
    print(True)

car = ['audi', 'bmw', 'honda', 'nissan']
my_car = 'dodge'
if my_car not in car:
    print(f'Car {my_car.title()}, is not list')