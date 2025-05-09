from trener import Car, Battery, ElectricCar

my_upgrade_battery = ElectricCar('tesla', 'model s', 2020)
my_upgrade_battery.battery.get_range()
my_upgrade_battery.battery.upgrade_battery()
my_upgrade_battery.battery.describe_battery()
my_upgrade_battery.battery.get_range()