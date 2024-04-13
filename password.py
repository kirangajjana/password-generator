import random

# List of letters from A to Z
letters = [chr(i) for i in range(65, 91)]

# List of numbers from 0 to 9
numbers = [str(i) for i in range(10)]

# List of symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

print("Hello! Welcome to the password generator.")

num_letters = int(input("Enter how many characters you want in your password: "))
num_numbers = int(input("Enter how many numbers you want in your password: "))
num_symbols = int(input("Enter how many symbols you want in your password: "))

# Generating password
password = []

for _ in range(num_letters):
    password.append(random.choice(letters))
# print(password)    

for _ in range(num_numbers):
    password.append(random.choice(numbers))
# print(password)      

for _ in range(num_symbols):
    password.append(random.choice(symbols))
# print(password)      

# Shuffle the password characters
random.shuffle(password)
# print(password)

# Convert password list to string
password_str = ''.join(password)
print("Generated password:", password_str)
