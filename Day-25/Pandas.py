import pandas

data = pandas.read_csv("25thDay\Weather_data.csv")

print(data["temp"].mean())

print(data["temp"].max())

print(data[data["temp"] == data["temp"].max()])

monday = (data[data["day"] == "Monday"])
fer = monday.temp * 1.8 + 32

print(fer)

# Create a Dataframe from scratch

data_dict = {
    "Student" : ["Amy", "James", "Angela"],
    "Marks" : [99, 34, 67]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Data_dict.csv")