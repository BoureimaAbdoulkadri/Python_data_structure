import csv

with open('d:\\data\\departement.csv', mode='r') as dept:
    rd = csv.reader(dept, delimiter=',')
    for r in rd:
        print(r)