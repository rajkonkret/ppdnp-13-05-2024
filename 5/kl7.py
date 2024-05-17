from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobac.")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("kierr kier kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Kalsa Sowa
    """


# Po oznaczeniu klasy jako abstrakcyjna, nie można utworzyć obiektu z tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł Bielik", 50)  # Tu Orzeł Bielik Lecę z szybkością 50
# or1.latam()
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()  # Tu Kura domowa Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura domowa")  # Tu Kura domowa Ja nie latam
kur2.latam()
kur2.wydaj_odglos()  # Ko ko ko ko ko

or2 = Orzel("Bielik", 55)
or2.latam()  # Tu Bielik Lecę z szybkością 55
or2.wydaj_odglos()  # kierr kier kir
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sow = Sowa("Sowa", 0)

or2.polowanie()  # Tu Bielik Rozpoczynam polowanie
kur2.dziobanie()  # Tu Kura domowa Idę sobie podziobac.a
