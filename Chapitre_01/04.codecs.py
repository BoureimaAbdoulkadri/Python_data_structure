import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    for r in rd:
        print(r[1:3])