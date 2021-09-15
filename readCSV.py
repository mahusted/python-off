import csv
with open('C:/Users/mahus/Documents/GitHub/python-off/mmsa-icu-beds.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

