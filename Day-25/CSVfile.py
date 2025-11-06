# Reading CSV Files in Python

import csv

with open("25thDay\Weather_data.csv") as data_files :
    data = csv.reader(data_files)
    
    next(data)
    
    temperatures = []
    
    for row in data :
        temp = int(row[1])
        temperatures.append(temp)
    
    print(temperatures)    
 