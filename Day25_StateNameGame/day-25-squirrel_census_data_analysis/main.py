import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red = data[data["Primary Fur Color"] == "Cinnamon"]
red_count = len(red)

black = data[data["Primary Fur Color"] == "Black"]
black_count = len(black)

gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(gray)

squirrel_dict = {
    "Fur Color": ["red", "gray", "black"],
    "Count": [red_count, gray_count, black_count]
}

new_data = pandas.DataFrame(squirrel_dict)
new_data.to_csv("squirrel_count.csv")
