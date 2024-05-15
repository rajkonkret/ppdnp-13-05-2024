dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wyswietlenie kluczy
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietlenie wartości
for v in dictionary.values():
    print(v)

# Radek
# Kowalski

# wyswietlenie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
print("Radek", end='')  # RadekTomek
print("Tomek")  # RadekTomek bo w poprzednim print znak nowej lini był pusty
print("Następny")  # Następny - bo poprzedni print miał standartowy znak końca linii "\n"

dictionary_2 = {'name': "imie", 'company': "Orange"}

d = {}
for k, v in dictionary_2.items():
    d[v] = k

print(dictionary_2)  # {'name': 'imie', 'company': 'Orange'}
print(d)  # {'imie': 'name', 'Orange': 'company'}
print({value: key for key, value in dictionary_2.items()})  # {'imie': 'name', 'Orange': 'company'}
