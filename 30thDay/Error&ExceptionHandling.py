# Error and Exception Handling in Python

try :
    file = open("File.txt", "r")
except FileNotFoundError :
    file = open("File.txt", "w")
    file.write("Aadarsh Rai")
    print("Error related to files")
else :
    content = file.read()
    print(content)
finally :
    raise KeyError("This is an error that I made up.")
