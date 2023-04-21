import csv
path = "departement.csv"
with open(path, mode='r') as dept:
    rd = csv.reader(dept, delimiter=',')
    for r in rd:
        print(r)
#%%
