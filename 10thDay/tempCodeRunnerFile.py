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
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
    is_leap(year)
    if is_leap == True :
        months_days[1] = 29
    
    return months_days[month - 1]
        
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month) 
print(days)