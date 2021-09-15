import csv
# To execute the following, download the mmsa-icu-beds.csv file to your local
# machine and change the file path below to the directory where you copied it to
with open('C:/Users/<UPDATE FILE PATH HERE>/mmsa-icu-beds.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

