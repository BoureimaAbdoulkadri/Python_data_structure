import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    codes = tuple(r[1] for r in rd)
    dept.seek(0)
    departements = tuple(r[2] for r in rd)

melange = dict(zip(codes, departements))

print(melange['75'])

