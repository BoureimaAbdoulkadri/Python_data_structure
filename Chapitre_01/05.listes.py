import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

print(departements)
departements.extend(['Geneve', 'Vaud', 'Valais'])
print(departements)
