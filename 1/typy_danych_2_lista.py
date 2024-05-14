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
