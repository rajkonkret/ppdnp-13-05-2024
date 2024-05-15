# petle - możliwość wykonania wielokrotnie tego samego zadania
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # range() - 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    pass
    # print(_)

for i in range(20):
    print(i * 2)

# lotto
lista_kula = list(range(1, 50))

lista_wylosowane = []

for i in range(6):  # 0..5
    wyn = random.choice(lista_kula)  # losujemy liczbę
    lista_kula.remove(wyn)  # usunięcie wylosowanej z listy
    print(wyn)  # wyświetlenie wylosowanej
    lista_wylosowane.append(wyn)

print(lista_wylosowane)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:
    if c > 10:
        print("Większe od 10", c)
    print(c)

# jak porównac liste z lista
lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 1]
print(lista1 == lista2)  # True

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # do tyłu
    print(i)

for i in range(-10, 0):
    print(i)

for c in lista2:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', "Zenek", "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)

# wyswietlic z listy w postaci 0 Radek
for p in imiona:
    print(imiona.index(p), p)

for i in range(len(imiona)):  # range(4) 0..3
    print(i, imiona[i])

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)  # (0, 'Radek') - krotka

a, b = (0, 'Radek')
for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

# ludzie = ['Radek', 'Arek', 'Tomek', 'Krzysztof']
ludzie = ['Radek', 'Arek', 'Tomek', 'Krzysztof', "Kamila"]  # IndexError: list index out of range
wiek = [44, 55, 66, 25]

# wyswietlic dane z tych dwóch list jako imie wiek -> Radek 44
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
# Radek 44
# Arek 55
# Tomek 66
# Krzysztof 25

# zip() - łączenie kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Arek', 55)
# ('Tomek', 66)
# ('Krzysztof', 25)
for lu, w in zip(ludzie, wiek):
    print(lu, w)
# Radek 44
# Arek 55
# Tomek 66
# Krzysztof 25

# wyswietlic w postaci 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Arek', 55))
# (2, ('Tomek', 66))
# (3, ('Krzysztof', 25))
a, b = (3, ('Krzysztof', 25))
print(a)  # 3
print(b)  # ('Krzysztof', 25)
c, d = b
print(c)
print(d)
# (a, (c, d)) = (3, ('Krzysztof', 25))
a, (c, d) = (3, ('Krzysztof', 25))
print(a, c, d)  # 3 Krzysztof 25

for i, (p, w) in enumerate(zip(ludzie, wiek)):
    print(i, p, w)
# 0 Radek 44
# 1 Arek 55
# 2 Tomek 66
# 3 Krzysztof 25

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000014F8E9E2980>
# for zipp in zipped:
#     print(zipp)
# # <itertools.zip_longest object at 0x000001CEEC742980>
# # ('Radek', 44)
# # ('Arek', 55)
# # ('Tomek', 66)
# # ('Krzysztof', 25)
# # ('Kamila', None)
# print("-----")
# for i, w in zipped:
#     print(i, w)
zip_list = list(zipped)
for item in zip_list:
    print(item)

for i, w in zip_list:
    print(i, w)
# Radek 44
# Arek 55
# Tomek 66
# Krzysztof 25
# Kamila None
# zadanko domowe - dodać wyswietlanie z indeksem 0 Radek 44
