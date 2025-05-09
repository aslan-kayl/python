class User():
    login_attempts = 0
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        User.login_attempts += 1


    def describe_user(self):
        print(f"hi my name is {self.first_name} {self.last_name} i am {self.age} years old and i live in {self.location}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        print(f"login attempts {self.login_attempts}")

    def reset_login_increment(self):
        self.login_attempts = 0