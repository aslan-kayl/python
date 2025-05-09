# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over")
#
# my_dog = Dog('willie', 6)
# print(f"My dog\'s name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over")
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print(f"My dog\'s name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"My dog\'s name is {your_dog.name}.")
# print(f"My dog is {your_dog.age} years old.")
# your_dog.roll_over()

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can\'t roll back an odometer")
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can\'t roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(25_000)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            next_range = 260
        elif self.battery_size == 100:
            next_range = 315
        print(f"This car can go about {next_range} milles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

class Hybrid(Car):
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity

bwd_hybrid = Hybrid(year=1999, make="fefe", model="dwqdq", fuel_capacity=50)

print(bwd_hybrid.year)

my_dict = {
    "name":"gg",
    "age":24,
    "grade": "high"
}

# my_dict['name'] = 'kolya'
# my_dict['age'] = 26
# print(f"My new name {my_dict['name'].title()}\n and age {my_dict['age']}")


