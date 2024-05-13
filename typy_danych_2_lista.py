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
