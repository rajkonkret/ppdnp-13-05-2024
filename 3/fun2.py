# funkcje zwracające wynik
def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(8, 9))  # 17
wyn = dodaj(8, 7)
print("Wynik:", wyn)  # Wynik: 15
print(odejmij())
print(odejmij(1))
print(odejmij(11, 2))
print(odejmij(11, 2, 5))
print(odejmij(b=9, c=8))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 45))
print(oblicz_vat(vat=14, cena=9000))
# 1230.0
# 1450.0
# 10260.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0

if zm == 1230:
    print("Działa")  # Działa

print(dodaj(6, 10) + odejmij(76, 4, 67))  # 21
