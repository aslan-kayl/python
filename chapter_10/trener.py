# with open ('test_directory/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())
from xml.etree.ElementTree import canonicalize

from chapter_10.write_message import filename

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())


# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(f"{pi_string[:50]}...")
# print(len(pi_string))
#
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love crating new games.\n")

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can\'t divide by zero")

# print("Give me two numbers, and I\'ll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst_number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can\'t divide by 0!")
#     else:
#         print(answer)

"""подсчёт приблизительного количество строк в файле"""
# def count_words(filename):
#
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#     else:
#         words = contents.split()
#
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
#
# filename = ['alise_in_wonderland.txt',
#             'learning_python.txt',
#             'my_guest.txt',
#             'programming.txt',
#             'pi_digits.txt'
#             ]
#
# for filenames in filename:
#     count_words(filenames)

import json

# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'numbers.json'
#
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)
#
# print(numbers)

# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
#
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We\'ll remember you when you come back, {username}!")
#
# else:
#     print(f"Welcome back, {username}!")

def greet_stored_user():
    """приветствует пользователя по имени"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = greet_stored_user()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We\'ll remember you when you come back, {username}!")

greet_user()