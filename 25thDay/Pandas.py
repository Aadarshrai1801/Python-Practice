import pandas

data = pandas.read_csv("25thDay\Weather_data.csv")

print(data["condition"])

data_dict = data.to_dict()

print(data_dict)