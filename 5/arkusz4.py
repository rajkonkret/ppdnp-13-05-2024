import pandas as pd

lista = [[2, 5, 8, 9], [9, 8, 5, 4]]

zbior = pd.DataFrame(lista)
zbior.columns = ['jeden', 'dwa', 'trzy', 'cztery']
print(zbior)
#    jeden  dwa  trzy  cztery
# 0      2    5     8       9
# 1      9    8     5       4

zbior.to_csv('test1.csv')

slownik = {'Imie': ['Ania', 'Radek', 'Tomek'], 'wiek': [18, 25, 76]}
sl = pd.DataFrame(slownik)
print(sl)
#     Imie  wiek
# 0   Ania    18
# 1  Radek    25
# 2  Tomek    76

sl.to_csv('test2.csv', sep=";")
sl.to_csv('test3.csv', sep=";", index=False)
