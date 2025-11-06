states_of_india = ["Uttar Pradesh", "Bihar", "Assam", "Odisha", "Tamil Nadu", "Rajasthan", "Andhra Pradesh", "Karnataka", "Kerala", "Madhya Pradesh", "Arunachal Pradesh", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Maharashtra", "Meghalaya", "Manipur", "Mizoram", "Nagaland", "Punjab", "Sikkim", "Telangana", "Tripura", "Uttrakhand", "West Bengal"]

states_of_india.append("AadarshLand")
states_of_india.extend(["RiteshLand", "PriyanshuLand"])

print(states_of_india)

# Day 4-2-Exercise

import random

names_string = input("Give me everybody's name, seperated by a comma. ")

names = names_string.split(",")

print(names)

num_items = len(names)

random_int = random.randint(0, num_items - 1)

# random_names = random.choice(names)

print(f"Person who is going to pay for today's meal is {names[random_int]}") 


# Nested Lists

# dirty_dozen = ["Spinach", "Strawberries", "Mustards", "Grapes", "Peaches", "Cherries", "Nectarines", "Pears", "Apples", "Blackberries", "Blueberries", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# Day 4-3-Exercise

row1 = ["😀", "😇", "🫢"]
row2 = ["🫢", "🤩", "🥲"]
row3 = ["🤕", "🤡", "🤑"]

map = [row1, row2 , row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

# if vertical == 1 :
#     if horizontal == 1 :
#         row1[0] = 'x'
#     elif horizontal == 2 :
#         row1[1] = 'x'
#     elif horizontal == 3 :
#         row1[2] = 'x'

# elif vertical == 2 :
#     if horizontal == 1 :
#         row2[0] = 'x'
#     elif horizontal == 2 :
#         row2[1] = 'x'
#     elif horizontal == 3 :
#         row2[2] = 'x'

# elif vertical == 3 :
#     if horizontal == 1 :
#         row3[0] = 'x'
#     elif horizontal == 2 :
#         row3[1] = 'x'
#     elif horizontal == 3 :
#         row3[2] = 'x'  

selected_row = map[vertical - 1] 
selected_row[horizontal - 1] = 'X'     

print(f"{row1}\n{row2}\n{row3}")



