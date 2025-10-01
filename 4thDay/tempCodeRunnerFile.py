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