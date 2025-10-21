import pandas

data = pandas.read_csv("25thDay\Weather_data.csv")

print(data["condition"])