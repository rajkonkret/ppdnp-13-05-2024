user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - liczba zmiennoprzecinkowa - rzeczywista
print(type(wersja))  # <class 'float'>
liczba = 123456789123
print(type(liczba))

print("Witaj %s masz teraz %d lat." % (user, wiek))
# Witaj Tomek masz teraz 39 lat.
# w takim sposobie wyświetlania python sprawdza typy
# print("Witaj %s masz teraz %d lat." % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit

print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})  # Witaj Tomek, masz teraz 39 lat.
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})  # Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Witaj Tomek, masz teraz 39 lat.
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
# Zaokrągla przy wyświetlaniu
print("Używamy wersji pythona %.0f" % 3.9)
print("Używamy wersji pythona %.f" % 3.9)
print("Wynik = %.2f" % 3.876)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X się nie zmieniło", x)  # X się nie zmieniło 3.14

y = round(x)  # zaokrąglenie w sensie matematyczne
print("y =", y)  # y = 3
print("x =", x)  # x = 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek" wyrównaj do prawej na długość 10 znaków
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 123456789123
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 123,456,789,123
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 123 456 789 123
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 123.456.789.123

print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,789,123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 123 456 789 123
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 123.456.789.123

liczba_2 = 123_456_789_900
print(liczba_2)  # 123456789900
print(type(liczba_2))  # <class 'int'>
print(f"Nasza duża liczba {liczba_2:,}".replace(",", " "))  # Nasza duża liczba 123 456 789 900
