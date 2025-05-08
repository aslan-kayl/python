from pydoc import describe


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"I work at the restaurant {self.restaurant_name} "
            f"it serves {self.cuisine_type} cuisine. ")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        print(f"List of ice cream varieties {self.flavors}")

my_icecream = IceCreamStand('gelato', 4, ['chocolate', 'vanilla'] )
my_icecream.describe_restaurant()
my_icecream.get_flavors()

# my_restaurant = Restaurant('katana', 8)
# my_restaurant.describe_restaurant()