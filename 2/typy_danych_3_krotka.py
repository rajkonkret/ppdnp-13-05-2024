# krotka - kolekcja, jest niemutowalna
# krotka jednoelementowa - zmienna - niezmienna - stałą

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

tupla_names = "Radek", "Tomek", "Zenek", "Marek"
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Marek')
print(type(tupla_names))  # <class 'tuple'>
tupla_names_2 = ("Radek", "Tomek", "Zenek", "Marek")
print(type(tupla_names_2))

tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>

# PEP8 wskazuje aby tuplę jedolelementową budować z nawiasami
tupla_4 = ("Radek",)
print(tupla_4)  # ('Radek',)
print(type(tupla_4))  # <class 'tuple'>

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla_liczby[2] = 0  # TypeError: 'tuple' object does not support item assignment

print(tupla_names.count("Tomek"))  # 1
print(tupla_names.index("Tomek"))  # 1

# sortowanie zwróci posortowaną listę
print(sorted(tupla_names))  # ['Marek', 'Radek', 'Tomek', 'Zenek']
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Marek')

# del(tupla_names[0])  # TypeError: 'tuple' object doesn't support item deletion
del tupla_liczby  # usunięcie elementu z pamięci
# print(tupla_liczby[0])  # NameError: name 'tupla_liczby' is not defined

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = tup
print(a)  # 1
print(b)  # 2

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3
print("a=", a, "b=", b)  # a= 1 b= [2, 3]

print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Marek')
imie1, *imie2, imie3 = tupla_names
print("imie1=", imie1, "imie2=", imie2, "imie3=", imie3)
# imie1= Radek imie2= ['Tomek', 'Zenek'] imie3= Marek

*imie1, imie2, imie3 = tupla_names
print("imie1=", imie1, "imie2=", imie2, "imie3=", imie3)
# imie1= ['Radek', 'Tomek'] imie2= Zenek imie3= Marek

imie1, imie2, *imie3 = tupla_names
print("imie1=", imie1, "imie2=", imie2, "imie3=", imie3)
# imie1= Radek imie2= Tomek imie3= ['Zenek', 'Marek']
# * worek na pozostałe dane

print(len(tupla_names_2))  # długość tupli - 4

lista = list(tupla_names_2)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek']
print(type(lista))  # <class 'list'>
