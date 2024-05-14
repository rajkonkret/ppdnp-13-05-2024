# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku (True lub False) wykonuje odpowiednie działanie

odp = True
# odp = False

if odp:
    print("Brawo")  # ten blok wykona się gdy odp będzie True
    print()
    print()
    print()
    print()
    print()

print("Dalsza część programu")

odp = "Radek"
if odp == "Radek":  # == porównanie
    print("To jest Radek")

odp = False
if odp:  # bool("Radek") -> True
    print("To jest", odp)
else:  # wartość domyślna
    print("False")

print("Kolejna dalsza część programu")
# Brawo
#
#
#
#
#
# Dalsza część programu
# To jest Radek
# False
# Kolejna dalsza część programu

podatek = 0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.6
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {zarobki * podatek}")
# dodać przedział od 10000 do 29999 podatek 0.2
# kolejnośc warunków w drzewku ma znaczenie
# pierwszy spełniona oznacze wyjście z konstrukcji if

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabacik = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25
