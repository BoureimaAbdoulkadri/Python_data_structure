import csv
import codecs

with codecs.open('departement.csv ', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

t1 = tuple(departements)
t2 = (12, 6)

d1 = {t2: 'roi'}

print(d1)