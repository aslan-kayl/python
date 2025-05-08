class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"I work in the restaurant {self.restaurant_name}, which has been there for {self.number_served} years already. ")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

    def read_number_served(self):
        print(f"Number of guests served: {self.number_served}")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, value_served):
        self.number_served += value_served

restaurant = Restaurant('Victor', 6)
# print(f"The restaurant {restaurant.restaurant_name} "
#       f"is already {restaurant.cuisine_type} years old. ")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()

restaurant.set_number_served(12)
restaurant.read_number_served()

restaurant.increment_number_served(21)
restaurant.read_number_served()