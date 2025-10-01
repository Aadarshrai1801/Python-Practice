import random

print("Welcome to  the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+', '&']

no_of_letter = int(input("How many letters would you like in your password?\n"))

no_of_symbol = int(input("How many symbols would you like?\n"))

no_of_number = int(input("How many numbers would you like?\n"))

string_password = []

for string in range(1, no_of_letter + 1) :          
    # Can use '_' in place of number
    random_string = random.choice(letters)
    string_password += random_string
# print(string_password) 

symbol_password = []

for symbol in range(1, no_of_symbol + 1) :     
    # Can use '_' in place of symbol
    random_symbol = random.choice(symbols)
    symbol_password += random_symbol
# print(symbol_password) 

number_password = []

for number in range(1, no_of_number + 1) :     
    # Can use '_' in place of number
    random_number = random.choice(numbers)
    number_password += random_number
# print(number_password)   

random_password = string_password + symbol_password + number_password

# print(f"The password of easy level is : {random_password}")

random.shuffle(random_password)

password = ""
for string in random_password :
    password += string

print(f"The password is : {password}")



