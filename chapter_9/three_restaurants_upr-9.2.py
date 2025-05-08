class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"The restaurant {self.restaurant_name} "
            f"is already {self.cuisine_type} years old. ")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")


restaurant = Restaurant('Victor', 6)
print(f"The restaurant {restaurant.restaurant_name} "
      f"is already {restaurant.cuisine_type} years old. ")

print(f"The restaurant {restaurant.restaurant_name} is open.")

restaurant = Restaurant('Gindza', 12)
print(f"The restaurant {restaurant.restaurant_name} "
      f"is already {restaurant.cuisine_type} years old. ")

print(f"The restaurant {restaurant.restaurant_name} is open.")

restaurant = Restaurant('Katana', 4)
print(f"The restaurant {restaurant.restaurant_name} "
      f"is already {restaurant.cuisine_type} years old. ")


print(f"The restaurant {restaurant.restaurant_name} is open.")
