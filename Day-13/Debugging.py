# Describe the problem

def myFunction() :
    for i in range(1,21) :
        if i == 20 :
            print("You got it")

myFunction() 

# Reproduce the bug

from random import randint

dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# Play Computer

year = int(input("What is your year of birth? "))
if year >= 1980 and year <= 1994 :
    print("You are a millenial.")

elif year > 1994 :
    print("You are a Gen Z.")

# Fix the Errors

age = int(input("How old are you? "))
if age >= 18 :
    print(f"You can drive at the age of {18}.")

# Print is my friend

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"No of pages: {pages}")
print(f"No of word per page: {word_per_page}")
print(total_words) 

# Use a Debugger

def mutate(a_list) :
    b_list = []
    for items in a_list :
        new_item = items * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 4, 5]) 

''' Tips for Debugging
        |
        |
        \/
    Tap a break or nap
    Ask for friend
    Run Often
    Ask StackOverFlow '''


# Day 13-1-Exercise

numbers = int(input("Which number do you want to check? "))

if numbers % 2 == 0 :
    print("This is an even number.")

else :
    print("This is an odd number.")


# Day 13-2-Exercise

year = int(input("Which year do you want to check? "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("It is a leap year.")
        else :
            print("It is not a leap year.")
    else :
        print("It is a leap year.")
else :
    print("It is not a leap year.")                    