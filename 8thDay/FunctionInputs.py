# Function with inputs

def greet(name) :
    print(f"Hello, {name}")
    print("How are you?")
    print("Are you doing good?")

greet("Angela") 

def greet_with(name, location) :
    print(f"Hello, {name}")
    print(f"Are you from {location}?")

greet_with(location = "London", name = "John")  

# Day 8-1-Exercise

import math

def paint_calc(height, width, cover) :
    print(f"No. of can would be required is {math.ceil((height * width)  / cover)}.")

test_h = int(input("Enter the height of the wall:\n"))    
test_w = int(input("Enter the width of the wall:\n"))

coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)

# Day 8-2-Exercise

def prime_checker(number) :

    is_prime = True

    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False
    print(is_prime)

    if is_prime :
        print("It is a prime number!")

    else :
        print("It is not a prime number!")     
           

n = int(input("Check this number:\n"))

prime_checker(number = n)