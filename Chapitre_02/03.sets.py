import csv
import codecs

with codecs.open('departement.csv ', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = set(r[2] for r in rd)

departements.add('Valais')
departements.update(['Vaud', 'Valais'])

if 'Vaud' in departements: departements.remove('Vaud')
departements.discard('Vaud')

suisse = frozenset(['Valais', 'Vaud', 'Geneve', 'Neuchatel'])
lesv = set(['Valais', 'Vaud'])

print(len(departements & suisse))
print(len(departements | suisse))
print(suisse - departements)
print(len(suisse ^ departements))
print(lesv <= suisse)
print(departements)
