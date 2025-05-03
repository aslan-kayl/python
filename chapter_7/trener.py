# height = int(input("How tall are you, in inches? "))
# if height >= 48:
#     print("\nYou\'re tall enough to ride!")
# else:
#     print("\nYou\'ll be able to ride when you\'re a little older.")

# number = int(input("Enter a number, and I'll tell you if it\'s even or odd: "))
# if number % 2 == 0:
#     print(f"\n The number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# current_number = 1
# while current_number <= 15:
#     print(current_number)
#     current_number += 1


# promt = "\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(promt)
#     print(message)
#
#     if message != 'quit':
#         print(message)

# promt = "\nPlease enter the name of a city you have visited:"
# promt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(promt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I\'d love to go to {city.title()}!")

current_number = 0
while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)