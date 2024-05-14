# kolekcje
# lista - przechowuje wiele danych, róznego typu na raz
# zachowuje kolejność przy dodawaniu elementów do listy

lista = []  # pusta lista
print(lista)  # [] dane typu lista
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elemntów na końcu listy
lista.append("Radek")
lista.append("Maciek")
lista.append("Zenek")
lista.append("Krzysztof")
print(lista)  # ['Radek', 'Maciek', 'Zenek', 'Krzysztof']
#                   0(-4)    1(-3)     2(-2)    3(-1)
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(len(lista))  # długość listy -> 4
print(lista[3])  # Krzysztof
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])  # Krzysztof
# Wypisac fragment listy, slicowanie
print(lista[0:3])  # ['Radek', 'Maciek', 'Zenek'] - indeksy 0, 1, 2
print(lista[:3])  # ['Radek', 'Maciek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Krzysztof'] indeksy 2, 3
print(lista[:])  # ['Radek', 'Maciek', 'Zenek', 'Krzysztof']
print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'Maciek']
print(lista[2:3])  # ['Zenek']
print(lista[2:10])  # ['Zenek', 'Krzysztof']
print(lista[7:10])  # []
print(lista[2:2])  # []
print(lista[0:3:2])  # ['Radek', 'Zenek']  # start:stop:krok

lista_10 = list(range(15))  # generuje liczby z zakresu 0..14
print(lista_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_10[-10:])  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14] dziesieć ostatnich elementów

# nadpisanie elemntu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Krzysztof']
# lista[10] = "Krzysztof"  # IndexError: list assignment index out of range

# wstawic element we wskazane miejsce (indeks)
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Krzysztof']
lista.insert(5, "Marek")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Krzysztof', 'Marek']
lista.insert(11, "Janek")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Krzysztof', 'Marek', 'Janek']

# sprawdzenie indeksu elementu
print(lista.index("Janek"))  # 6
indeks = lista.index("Maciek")

# usunięcie elementu po elemncie (o niższym indeksie)
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Krzysztof', 'Marek', 'Janek']
lista.append("Radek")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Krzysztof', 'Marek', 'Janek', 'Radek']
print(lista.remove("Radek"))  # None - remove nie zwraca wyniku
print(lista)  # ['Marcin', 'Maciek', 'Krzysztof', 'Marek', 'Janek', 'Radek']

# usunięcie elementu po indeksie
indeks = lista.index("Maciek")
lista.pop(indeks)
print(lista)  # ['Marcin', 'Krzysztof', 'Marek', 'Janek', 'Radek']
print(lista.pop(0))  # Marcin - pop() zwraca usunięty element
print(lista)  # ['Krzysztof', 'Marek', 'Janek', 'Radek']

print(lista.pop())  # Radek - usunie ostatni element z listy
print(lista)  # ['Krzysztof', 'Marek', 'Janek']
print(lista.pop(-2))  # Marek

a = 1
b = 3
a = b
print(a)  # 3
b = 7
print(a)  # 3

lista_2 = lista  # a = b, kopiowanie adresu (referencji)
lista_copy = lista.copy()  # kopiowanie elementów jedej listy do drugiej
print(lista)  # ['Krzysztof', 'Janek']
print(lista_2)  # ['Krzysztof', 'Janek']
print(lista_copy)  # ['Krzysztof', 'Janek']
lista.clear()  # b = 7
print(lista)  # []
print(lista_2)  # [], obie wskazuja na ten sam obszar pamieci, zmiana następuje w obu
print(lista_copy)  # ['Krzysztof', 'Janek']
print(id(lista))  # 2021573382528
print(id(lista_2))  # 2021573382528
print(id(lista_copy))  # 2021576213952

# liczby = [54, 999, 34, 22, 12.34, 687]
# liczby = [54, 999, 34, 22, 12.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
liczby = [54, 999, 34, 22, 12.34, 687, True]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(type(liczby))  # <class 'list'>
print(liczby)  # [54, 999, 34, 22, 12.34, 687]

liczby.sort()  # dla list string-int TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)  # [12.34, 22, 34, 54, 687, 999] - zmienia bazowa kolekcję
print(liczby)  # [True, 12.34, 22, 34, 54, 687, 999] dla listy z bool

lista_osob = ['radek', 'ola', 'agata', 'lena']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']
lista_osob.sort(reverse=True)  # sortuje i odwraca kolejność
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']

# kody ascii dla znaku "A" i "a"
print(ord("A"))  # 65
print(ord("a"))  # 97
print("radek".capitalize())  # Radek

liczby.reverse()  # odwrócenie listy
print(liczby)  # [999, 687, 54, 34, 22, 12.34, True]

liczby[3] = 6666
print(liczby[0:3])  # [999, 687, 54]
print(liczby[-2])  # 12.34
print(liczby[-3:])  # [22, 12.34, True]
print(liczby)  # [999, 687, 54, 6666, 22, 12.34, True]

liczby.remove(54)
print(liczby)  # [999, 687, 6666, 22, 12.34, True]

print(liczby.pop(2))  # 6666
print(len(liczby))  # 5

print(liczby)  # [999, 687, 22, 12.34, True]
print(liczby[0:4:2])  # [999, 22]
print(liczby[::-1])  # odwrócona lista [True, 12.34, 22, 687, 999]

tekst = "Pyt hon."
lista1 = list(tekst)  # list() - rzutownie na liste, rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', ' ', 'h', 'o', 'n', '.']

lista3 = [tekst]
print(lista3)  # ['Python']

liczba = 123456
# print(list(liczba))  # TypeError: 'int' object is not iterable
print([liczba])  # [123456]

krotka = tuple(liczby)  # tuple() - rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 687, 22, 12.34, True)
