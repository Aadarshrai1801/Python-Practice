# For Loop

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits :
    print(fruit)
    print(fruit + "Pie")
    print(fruits)

# Day 5-1-Exercise

students_height = input("Enter the list of students height :").split()
# print(students_height)

for n in range(0, len(students_height)) :
    students_height[n] = int(students_height[n])

total_height = 0     
for height in students_height :
    total_height = total_height + height
# print(total_height)

total_student = 0
for student in students_height :
    total_student = total_student + 1
print(total_student)  

average_height = round(total_height / total_student)

print(average_height)

# Day 5-2-Exercise

student_scores = input("Enter the marks of the student in the class :\n").split()

for n in range(0, len(student_scores)) :
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_score = 0
for score in student_scores :
    if score > max_score :
        max_score = score

print(f"The highest score in the class is :{max_score}")   

# For Loop and the range() function

total_count = 0
for n in range(1,101) :
    total_count += n

print(total_count)    

# Day 5-3-Exercise

total_sum = 0
for num in range(1,101) :
    if num % 2 == 0 :
        total_sum += num

print(f"Sum of all even numbers between 1 and 100 is : {total_sum}")


# Day 5-4-Exercise

for num in range(1,101) :
    if num % 3 == 0 and num % 5 == 0 :
        print("FIzzBuzz")
    elif num % 3 == 0 :
        print("Fizz") 
    elif num % 5 == 0 :
        print("Buzz")
    else :
        print(num)       
