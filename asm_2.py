import csv
import numpy as np
import re
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
data_set = []
for row in csv.reader(open("csv_file/GrocerySales.csv"), delimiter=","):
    data_set.append(row)
print(data_set)

for i in range (1, len(data_set)):
    for j in range(0, len(data_set[i])):
        x = re.findall("[!@#$%^&*?]", data_set[i][j]) #
        if data_set[i][j] == '' or data_set[i][j] == ' ':
            data_set[i][j] = '0'
        if x:
            data_set[i][j] = '0'
print(data_set)

f = open("file_cleaned.csv","w")
for i in range (1, len(data_set)):
    for j in range(0, len(data_set[i])):
        f.write(data_set[i][j] + ",")
    f.write("\n")
f.close()

