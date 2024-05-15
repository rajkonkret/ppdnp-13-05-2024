# funkcja - wydzielony fragment kodu, można go wykonać wielokrotnie
# można wywołąć w dowolnym momencie
# deklaracja funkcji musi być wcześnij niż wywołanie
# w miejscu deklaracji funkcja się nie wykonuje

a = 9
b = 8


# deklaracja funkcji - tu kod się nie wykonuje
def dodaj():  # Funkcja bez argumentów
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami: a i b, przekazanie obowiązkowe
    print(a + b)


# funkcja z argumentami o wartości domyslnej c=0
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()  # nazwa funkcji i ()  17
# dla dodaj2() musimy przekazać obowiązkowo dwa argumenty
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(15, 45)  # 60
odejmij(8, 9)
odejmij(8, 9, 25)  # argumenty pozycyjne
odejmij(b=9, a=9, c=23)  # -23 argumenty po nazwie
odejmij(b=9, a=9)  # 0
odejmij(5, c=9, b=12)  # -16 mieszane
# odejmij(a=7, b=9, 7)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None
# print(dodaj() + dodaj2(6, 4))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
