import csv
import codecs

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])

departements.extend(['Geneve', 'Vaud', 'Valais'])

departements += 'Neuchatel'

# l1, l2 = departements[0], departements[1]
# l1, *l2 = departements

# l1, l2 = departements[]
#
# print(l1)
# print(l2)

l1 = departements[-len('Neuchatel'):]

print(''.join(l1))



