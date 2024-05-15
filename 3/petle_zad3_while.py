# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print(licznik, "Komunikat1!")
    if licznik > 10:
        break
print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Drugi komunikat !! !! !!")

# deepl

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['5', '6', '7', '810']
# [5, 6, 7, 810]
