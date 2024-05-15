import csv

fields = []
rows = []

filename = 'records.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter, dialect.quotechar)  # ; "
    f.seek(0)  # ustawienie odczytu pliku na 0
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    # print(csvreader)
    fields = next(csvreader)  # odczytuje bieżący element i przestawia odczyt na następny
    for row in csvreader:
        # print(row)
        rows.append(row)

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)
# [['radek', 'coe', '3', '9.1'], ['tomek', 'cos', '2', '19.1'], ['zenek', 'cot', '4', '9.10'],
#  ['Krzysztof', 'cor', '1', '11']]
