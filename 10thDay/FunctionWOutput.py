# Function with Output

def format_name(f_name, l_name) :
    t_name = f_name.title() + " " + l_name.title()
    return t_name

output = format_name("AaDaRsH", "RaI")
print(output)

# Day 10-1-Exercise

def is_leap(year) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return True
            else :
                return False
        else :
            return True
    else :
        return False

def days_in_month(year, month) :
    
    if month > 12 or month < 1 :
        return "Invalid Input"

    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
    if is_leap(year) and month == 2 :
    #   months_days[1] = 29
        return 29
    
    return months_days[month - 1]
        
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month) 
print(days)  
