# Password generator
# In this project you will write your own password generator. Program asks the user to input password lenght. Then generate random passwords with lower case letters, upper case letters, digits and special characters. In the basic version you don't don't have to worry about whether your randomly generated password contains at least one character from every set, but you can also think about how to do it!

# Hints:
# Object string has builded-in constance strings you can use in your program:
# string.ascii_letters # Concatenation of the ascii (upper and lowercase) letters
# string.ascii_lowercase # All lower case letters
# string.ascii_uppercase # All Upper case letters
# string.digits  # The string ‘0123456789’.
# string.punctuation  # String of ASCII characters which are considered special characters.

# You can concatenated strings you need and choose a random character using:
# random.choice(string_with_all_characters)

import random
import string


char = []
password = []

dictionary = string.punctuation+string.digits+string.ascii_letters

for i in dictionary:
    char.append(i)

numbers_of_characters = input("Enter number of lenght password: ")          #
if not numbers_of_characters.isdigit():                                     #
    print("Please enter number of your password.")
else:
    numbers_of_characters = int(numbers_of_characters)
    for i in range(numbers_of_characters):
        password.append(random.choice(char))
    random.shuffle(password)
    password_str = "".join(password)
    print(f"""=================================================================
(っ◔◡◔)っ Your new password is: " {password_str} " have fun! (っ◔◡◔)っ 
=================================================================""")
    question = input("Do you want to generate again? y/n").lower()
    if question != "y":
        print("""
        Have a good day 😎✋""")
