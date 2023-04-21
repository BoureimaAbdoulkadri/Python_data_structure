import csv
import codecs
import collections

with codecs.open('departement.csv ', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    codes, departements = zip(*((r[1], r[2]) for r in rd))

test = collections.Counter(d[0] for d in departements)

test = collections.deque
test.appendleft('coucou')
test.popleft()
test.count()
test.rotate(1)

print(test.most_common(5))
