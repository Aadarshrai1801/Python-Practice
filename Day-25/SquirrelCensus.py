# 2018 Squirrel Census 

import pandas

data = pandas.read_csv("25thDay\Squirrel_data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]

no_of_grey = gray.shape[0]

print(no_of_grey)

black = data[data["Primary Fur Color"] == "Black"]

no_of_black = black.shape[0]

print(no_of_black)

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]

no_of_cinnamon = cinnamon.shape[0]

print(no_of_cinnamon)

data_dict = {
    "Fur Color" : ["Gray", "Black", "Red"],
    "Count" : [f"{no_of_grey}", f"{no_of_black}", f"{no_of_cinnamon}"]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("Data2")