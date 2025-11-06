# Types of arithmetic operators 

#    Parenthesis : ()
#    Power : * * 
#    Multiplication : * 
#    Division : /
#    Addition : +
#    Subtraction : -

# Day 2-3-Exercise

height = input("Enter your height in m :\n")
weight = input("Enter your weight in kg :\n")

calc_height = float(height)
calc_weight = float(weight)

bmi = int(calc_weight/ calc_height**2)
print("Your BMI is ",bmi)


   