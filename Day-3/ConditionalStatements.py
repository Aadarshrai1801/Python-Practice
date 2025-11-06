# Conditional Statements

print("Welcome to the roller coaster ride! ")

height = int(input("Enter your height here : "))

bill = 0

if height >= 120 :
    print("Yes, you can take a ride here!")
    age = int(input("Enter your age here :"))
    if age < 12 :
        bill = 5
        print("Your ticket price is $5!")
    elif age <= 18 :
        bill = 7
        print("Your ticket price is $7!")   
    elif age <=30 :
        bill = 20
        print("Your ticket price is $20")
    elif age >= 45 and age <= 55 :
        bill = 0
        print("Your ticket price is free!")    
    else :
        bill = 12
        print("Your ticket price is $12!")
    
    pic = input("Do you want to take a photo? Y or N : ")
    if pic == "Y" :
        bill += 3
    print(f"The ticket price is : $ {bill}")  

else :
    print("Sorry, You are too short to take a ride here!")

# Day 3-1-Exercise

number = int(input("Enter the no. you want to check : "))

if number % 2 == 0 :
    print("This is an even number!")
else : 
    print("This is an odd number.")


# Day 3-2-Exercise

height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))

bmi = round( weight / height ** 2, 2 )

print(f"Your body mass index is {bmi}")

if bmi < 18.5 :
    print("You are underweight!")
elif bmi < 25 :
    print("You have a normal weight!")
elif bmi < 30 :
    print("You are overweight!")
elif bmi < 35 :
    print("You are obese!")
elif bmi > 35 :
    print("You are clinically obese!")      


# Day 3-3-Exercise

year = int(input("Enter the year of your wish:"))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("It is a leap year!")
        else :
            print("It is not a leap year!")    
    else :
        print("It is a leap year!")        
else :
    print("It is not a leap year!")  


# Day 3-3-Exercise

print("Welcome to the Python Pizza Deliveries !")

size = input("What size of pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S" :
    bill += 15
    if add_pepperoni == "Y" :
        bill += 2

elif size == "M" :
    bill += 20
    if add_pepperoni == "Y" :
        bill += 3

elif size == "L" :
    bill += 25
    if add_pepperoni == "Y" :
        bill += 3

if extra_cheese == "Y" :
    bill += 1
    print(f"Your final bill is {bill}!")
    
else :
    print(f"Your Final bill is {bill}!")    

        












