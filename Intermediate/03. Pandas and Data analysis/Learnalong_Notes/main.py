# # data = []
# # with open("weather_data.csv")as f:
# #     for row in f:
# #
# #         file = f.readlines()
# #         data.append(file)
# #
# #
# # print(data)
# import csv
#
# with open("weather_data.csv") as csvfile:
#     reader = csv.reader(csvfile)
#     temprature = []
#     for row in reader:
#         if row[1] == "temp":
#             pass
#         else:
#             temprature.append(int(row[1]))
# print(temprature)
import pandas as pd

file = pd.read_csv("weather_data.csv")

# tempr = file["temp"].to_list()
#
# temps = 0
# for temp in tempr:
#     temps += int(temp)
# print(temps / len(tempr))
# print(file["temp"].max())

# print(file[file.day == "Monday"])
# print(file[file.temp == file.temp.max()])

monday =file[file.day == "Monday"]
print(monday.temp)
temp = monday.temp*9/5 + 32
print(temp)