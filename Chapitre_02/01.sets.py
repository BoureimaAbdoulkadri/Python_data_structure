import csv
import codecs

with codecs.open('departement.csv ', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = set(r[2] for r in rd)


print(departements)

#%%
