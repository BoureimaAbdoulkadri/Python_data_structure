import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

departements.extend(['Geneve', 'Vaud', 'Valais'])

# del(departements[0])
# departements.pop(departements.index('Aube'))
# departements.remove('Aube')
# departements.reverse()

# departements.sort(key=int)
# departements.sort(key=lambda l: l[-1])
departements.sort(key=lambda l: l[::-1])

print(departements)

