# funkcja lambda - skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, mozliwość deklaracji w miejscu wykonania

def odejmij2(a, b):
    return a - b


print(odejmij2(7, 8))  # -1

odejmij = lambda a, b: a - b  # domyślnie ma return
print(odejmij(10, 56))  # -46

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły

lista = [1, 2, 5, 34, 56, 100, 200, 500]
# wypisaniu z tej listy wartości pomnożonych przez 2

# print(lista * 2)  # [1, 2, 5, 34, 56, 100, 200, 500, 1, 2, 5, 34, 56, 100, 200, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 10, 68, 112, 200, 400, 1000]

print([i * 2 for i in lista])  # [2, 4, 10, 68, 112, 200, 400, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 10, 68, 112, 200, 400, 1000]

# funkcje wyższego rzędu
# map() - pobiera element z kolekcji, wykonuje na nim operację zadaną funkcją
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 10, 68, 112, 200, 400, 1000]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 10, 68, 112, 200, 400, 1000]
print(f"Zastosowanie map: {list(map(lambda x: x * 14, lista))}")
# Zastosowanie map: [14, 28, 70, 476, 784, 1400, 2800, 7000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - pobiera element, zwraca spełniający warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 50, lista))}")
# Zastosowanie filter(): [56, 100, 200, 500]
# x > 3 i x < 100
# x > 200
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 200, lista))}")
# Zastosowanie filter(): [500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
# Zastosowanie filter(): [5, 34, 56]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
