# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from numpy.ma import average

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data)) #prints <class 'pandas.DataFrame'>
temperatures = data["temp"]
# print(type(temperatures)) # prints <class 'pandas.Series'>

data_dict = data.to_dict()
# print(data_dict)

# average = data["temp"].mean()
# print(average)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data["condition"])
#
# print(data.condition)

# print(data[data.day == "Monday"])

# Find which day has the highest temperature
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp = monday.temp[0]
#
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# create data frame -
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76,56,65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

new_data.to_csv("new_data.csv")


