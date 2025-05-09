from car import Car
from my_electric_car import ElectricCar as EC

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_electric_car = EC('tesla', 'model s', 2020)
print(my_electric_car.get_descriptive_name())