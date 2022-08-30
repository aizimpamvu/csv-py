# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# with open("weather_data.csv") as data_file:
#     # data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list= data['temp'].to_list()
# print(len(temp_list))
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# print(data['temp'].mean())
# # data row
# print(data[data.day =="Monday"])
#
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# dataframe from scratch

# data_dict = {
#     "students": ["Alice", "Dan", "Tom"],
#     "scores": [67, 78, 92]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sqirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_sqirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_sqirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_sqirrel_count)

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_sqirrel_count, red_sqirrel_count, black_sqirrel_count]
}

sorted_data= pd.DataFrame(data_dict)
print(sorted_data)
sorted_data.to_csv("squirrel_count.csv")
