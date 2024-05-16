class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # Stworzyc dwie różne metody do wypisanie wieku i wzrostu
    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Radek", 56, 178, "m")
print("Imię", cz1.imie)  # Imię Radek
print("Wiek", cz1.wiek)  # Wiek 56
print("Płeć", cz1.plec)  # Płeć m
# cz2 = Human() TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1.powitanie()  # Nazywam się Radek
cz1.wypisz_wzrost()
cz1.wypisz_wiek()
# Mam 178 cm wzrostu
# Mam 56 lat
cz2 = Human("Anna", 34, 170)
cz1.ruszaj()
print("-----")
cz2.powitanie()
cz2.ruszaj()
# Ruszyłem w drogę
# -----
# Nazywam się Anna
# Ruszyłam w drogę
