from random import choice

lottery = [1462, 9835, '10mk', 'pa12', 'tj5a']
my_lottery = choice(lottery)
my_victory = 'tj5a'

# while True:
for lottery in my_lottery:
    if my_lottery == my_victory:
        print(f"Whoever gets these {my_victory} wins!!!")
    else:
        print(f"Sorry but luck is not on your side today")
    # break
print(my_lottery)