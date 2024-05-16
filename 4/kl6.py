# pracownik  - imie, nazwisko, pensja
# manager - imie, nazwisko, pensja, premia
# konstruktor
# przedstaw_sie()
# oblicz_pensje()
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    def oblicz_pensja(self):
        return self.pensja


class Manager(Pracownik):
    """
    Manager dziedziczy po Pracownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensja(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 4200)
pracownik.przedstaw_sie()
print("Pensja wynosi", pracownik.oblicz_pensja())

manago = Manager("Anna", "Nowak", 6000, 3000)
manago.przedstaw_sie()
print("Pensja wynosi", manago.oblicz_pensja())
# Nazywam się Jan Kowalski
# Pensja wynosi 4200
# Nazywam się Anna Nowak
# Pensja wynosi 9000
