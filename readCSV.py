import csv
with open('C:/Users/mahus/Dropbox/Python/ReadCSV/csv-1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

