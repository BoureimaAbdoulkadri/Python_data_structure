import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

departements.extend(['Geneve', 'Vaud', 'Valais'])
# departements.insert(2, ['Neuchatel', 'Jura'])

departements[2:2] = ['Neuchatel', 'Jura']

print(departements)
# print(departements.pop(0))
# print(departements)

