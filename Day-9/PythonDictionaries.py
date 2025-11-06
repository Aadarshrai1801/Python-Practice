# Python Dictionaries

programming_dictionary = { 
    "Bug" : "An error in a program that prevents the program from running as exprected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again." 
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding new items to dictionary
 
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

# Create an empty dictionary

empty_dictionary = {}


# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary

for thing in programming_dictionary :
    print(thing)
    print(programming_dictionary[thing])


# Day 9-1-Exercise

student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grade = {}

for student in student_score :
    if student_score[student] >= 91 :
        student_grade[student] = "Outstanding"

    elif student_score[student] >= 81 and student_score[student] <= 90 :
        student_grade[student] = "Exceeds Expectations"

    elif student_score[student] >= 71 and student_score[student] <= 80 :
        student_grade[student] = "Acceptable"

    elif student_score[student] <= 70 :
        student_grade[student] = "Fail"
        

print(student_grade)         