from random import randint

class Die():
    def __init__(self, sides=10):
       self.sides = sides

    def roll_die(self):
        my_roll_die = randint(1, 10)
        print(my_roll_die)
        # my_roll_die = 0

        # for i in my_roll_die:
        #     if i >= 11:
        #         print(f"{i}")

class Die2(Die):
    def __init__(self, sides=20):
        super().__init__(sides=20)
        self.sides = sides


my_die = Die(sides=10)
my_die.roll_die()

my_die2 = Die2()
my_die2.roll_die()