import csv
import codecs
import itertools

with codecs.open('d:\\data\\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    codes, departements = zip(*((r[1], r[2]) for r in rd))

# test = tuple(itertools.chain.from_iterable(departements))
# test = tuple(itertools.accumulate(codes))
# test = tuple(itertools.groupby(departements, key=len))
#
# for t in itertools.groupby(departements, key=len):
#     print(t[0], tuple(t[1]))

masque = tuple((d[0] < 'J' for d in departements))
print(masque)

test = tuple(itertools.compress(departements, masque))
print(test)