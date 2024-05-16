class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja - ustawienie pola jako prywatne
        self.__predkosc = 0  # __ pole prywatne

    # enkapsulacja - wystawienie metod do odczytu i zapisu pól
    def gaz(self):
        self.__predkosc += 10

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Ford", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# Po oznaczeniu jako pole prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50
car1.licznik()
car1.__predkosc = 0  # pole o widocznosci globalnej
car1.licznik()  # Prędkość wynosi 0 km/h, Prędkość wynosi 50 km/h
print(car1.__predkosc)  # 0
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# 0
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h
