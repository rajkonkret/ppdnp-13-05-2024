# klasa - przepis, szablon, stempel
# odcisk stempla - obiekt
# obiekt - instancja klasy - obiekt zbudowany poprzez wypełnienie cech przepisu, szablonu

# definicja klasy - nic się nie wykona
class Human:
    """
    Klasa Human definiująca człowieka Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt, który wyoła metode
    def powitanie(self):
        print("nazywam się", self.imie)


help(Human)  # wyswietlenie dokumentacji kalsy (zawartej w komentarzu)
# pydoc -b  - uruchomienia serwera z dokumentacją naszego projektu
# pydoc -w kl1 - wygenerowanie pliku html z dokumentacją dla pliku pythonowego

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x00000154D1558B00>
print(cz1.imie)
cz1.imie = "Radek"
print(cz1.imie)  # Radek
print(Human.__doc__)  # dokumentacja
#     Klasa Human definiująca człowieka Pythonie
print(print.__doc__)
cz1.wiek = 45
cz1.plec = "m"
print(cz1.wiek)  # 45
print(cz1.plec)  # m
print(cz1.imie)  # Radek

# stworzyc obiekt klasy Human odmiennej płci
cz2 = Human()
cz2.plec = "k"
cz2.wiek = 27
cz2.imie = "Anna"

print("Imię:", cz2.imie)  # Imię: Anna
print("Wiek:", cz2.wiek)  # Wiek: 27
print("Pleć:", cz2.plec)  # Pleć: k
cz2.powitanie()  # nazywam się Anna
