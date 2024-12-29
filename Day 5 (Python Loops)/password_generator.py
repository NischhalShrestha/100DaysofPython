import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator")

no_letters = int(input("How many letters do you want in your password"))
no_numbers = int(input("How many numbers do you want in your password"))
no_symbols = int(input("How many symbols do you want in your password"))

# password = ""

# for character in range(0,no_letters):
#     password =+ random.choice(letters)

# for character in range(0, no_numbers):
#     password =+ random.choice(numbers)

# for character in range(0, no_symbols):
#     password =+ random.choice(symbols)

# print(password)


password_list = []

for character in range(0, no_letters):
    password_list.append(random.choice(letters))

for character in range(0, no_numbers):
    password_list.append(random.choice(numbers))

for character in range(0, no_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)


password = ""
for character in password_list:
    password += character

print(f"Your password can be : {password}")

