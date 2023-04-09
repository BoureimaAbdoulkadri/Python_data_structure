import csv
import codecs
# from functools import reduce

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

l1 = list(map(lambda d: d.upper(), departements))
l2 = list(filter(lambda d: d[0] in ['A', 'H', 'J'] , departements))

print(l2)
