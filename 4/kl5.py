# dziedziczenie
# przejęcie cech innej klasy, nadpisanie, modyfikacja, rozszerzenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):  # klasa Samochod dziedziczy po klasie Pojazd
    """
    klasa samochód
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)  # musimy wyołąć konstruktor klasy wyższej super()
        self.marka = marka

    def info(self):
        super().info()  # mozęmy wywołać metode z klasy super
        print(f"Marka: {self.marka}")


poj = Pojazd("czerwony")
poj.info()  # Kolor: czerwony

car1 = Samochod('zielony')
car1.info()
# Kolor: zielony
# Marka: None
car2 = Samochod('czerwony', "Ferrari")
car2.info()
# Kolor: czerwony
# Marka: Ferrari

# polimorfizm - możliwośc wykorzystania obiektów różnych klas za pomocą cech wspólnych
lista = [poj, car1, car2]
for i in lista:
    i.info()
# Kolor: czerwony
# Kolor: zielony
# Marka: None
# Kolor: czerwony
# Marka: Ferrari
# Kolor: czerwony
# Kolor: zielony
# Marka: None
# Kolor: czerwony
# Marka: Ferrari
