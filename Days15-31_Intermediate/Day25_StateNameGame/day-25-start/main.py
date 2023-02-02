# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# mtemp_far = 1.8 * monday_temp + 32
# print(mtemp_far)

# create dataframe from scratch:
data_dict = {
    "students" : ["Amy", "James", "Jake"],
    "scores" : [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")