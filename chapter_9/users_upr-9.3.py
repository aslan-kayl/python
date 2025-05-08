class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        print(f"hi my name is {self.first_name} {self.last_name} i am {self.age} years old and i live in {self.location}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

my_user = User('aslan', 'kayl', 18, 'varkuta')
my_user.describe_user()
my_user.greet_user()

my_user = User('kasl', 'asl', 23, 'irkutsk')
my_user.describe_user()
my_user.greet_user()

my_user = User('kolya', 'askal', 29, 'baikal')
my_user.describe_user()
my_user.greet_user()