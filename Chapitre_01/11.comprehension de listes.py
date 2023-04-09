import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

# departements[:] = [d.upper() for d in departements]
l1 = [d.upper() for d in departements]

print(l1)

print(len(''.join(l1)))
print(sum(len(d) for d in departements))