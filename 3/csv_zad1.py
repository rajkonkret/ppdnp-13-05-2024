import csv

# pliki csv
# pliki w których dane są oddzielone są seperatorem (, tab ;)
# Radek, Maciek, Zenek

filename = 'records.csv'
row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'tomek', 'branch': 'cos', 'year': 2, 'cgpa': '19.1'},
    {'name': 'zenek', 'branch': 'cot', 'year': 4, 'cgpa': '9.10'},
    {'name': 'Krzysztof', 'branch': 'cor', 'year': 1, 'cgpa': '11'},
]

with open(filename, "w", newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()  # zapisanie nagłóków
    # csvwriter.writerow(dictionary)  # zapisanie słownika jako jeden wiersz
    csvwriter.writerows(dict_list)  # zapisanie listy słownikó jako wiele wierszy
