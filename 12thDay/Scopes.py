# NameSpace Scope vs Global Scope

enemies = 1

def count_enemies() :
    enemies = 2
    return enemies

print(count_enemies())
print(enemies)

age = 50 # Global Scope

def aadarsh() :
    global age
    age = 20  # Local Scope
    print(f"Age of Aadarsh is {age}")

aadarsh() # It will use the local scope.
print(f"Global age is {age}") # It will use global scope.

# Global Constants

PI = 3.14159

def calc() :
    print(PI)

calc()