# zrobić klasę Dom
# metraż, kolor, liczba_okien
# pola mają byc prywatne
# wystawić  metody do odczytu i zapisu tych pól
# dodać komentarz - dokumentacje
# użyc tej klasy do obiektów typu Dom
class Dom:
    """
    Klasa opisująca dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """

        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz} m2")

    def mam_okna(self):
        print(f"Liczba okien {self.__liczba_okien} szt")

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()
        self.__farba()

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.__liczba_okien = odp
        self.mam_okna()

    def __farba(self):
        print("Skończyła się farba")


dom1 = Dom(230, "biały", 16)
dom1.mam_okna()
dom1.mam_metraz()
dom1.mam_kolor()
# Liczba okien 16 szt
# Mam metraż 230 m2
# Mam kolor biały
dom1.zmien_metraz()
dom1.zmien_kolor()
dom1.zmien_okna()
