# set - zbiór - kolekcja, przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu
# w zbiorze nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - rzutowanie na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

zb2 = set()  # utworzenie pustego zbioru
print(zb2)  # set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięci eelementu za pomocą pop()
print(zbior.pop())  # 33 zwraca i usunie pierwszy element ze zbioru

# usunięcie po elemencie
zbior.remove(55)
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()  # kopiownie elementów do drugiego zbioru
print(zbior_copy)  # {66, 18, 22, 777, 11, 44} - zamienił kolejność

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# zwraca sumę zbiorow
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(zbior)  # {66, 777, 11, 44, 18, 22}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
zbior.add(0)
print(zbior)  # {0, 66, 777, 11, 44, 18, 22}
print(zbior.union(zbior_2))  # {0, 66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {0, 777, 66, 22}
print(zbior.difference(zbior_2))  # {0, 777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}
# {999, 11, 44, 12.34, 18, 52, 667, 62} - {0, 66, 777, 11, 44, 18, 22} = {999, 12.34, 52, 667, 62}

# łaczy zbiory - zamienia bazowy
zbior.update(zbior_2)
print(zbior)
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# róznica symetryczna
zbior_3 = {66, 777, 11, 44, 18, 22}
print(zbior_3 ^ zbior_2)  # {66, 999, 777, 12.34, 52, 22, 667, 62}
print(zbior_3.symmetric_difference(zbior_2))  # {66, 999, 777, 12.34, 52, 22, 667, 62}

lista = list(zbior_3)
print(lista)  # [66, 18, 22, 777, 11, 44]

krotka = tuple(zbior_3)
print(krotka)  # (66, 18, 22, 777, 11, 44)
