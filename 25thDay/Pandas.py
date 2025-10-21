import pandas

data = pandas.read_csv("25thDay\Weather_data.csv")

print(data["temp"].mean())

print(data["temp"].max())