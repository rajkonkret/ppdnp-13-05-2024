# funkcja obliczająca średnią
# name, *cyfry = ("Radek", 4, 5, 5, 6, 5, 4)


def liczby(name=None, *cyfry):  # przyjmuje dowolną ilośc argumentów pozycyjnych
    print(cyfry)
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except (ZeroDivisionError, TypeError) as e:
        print("Dzielenie przez zero lub błąd typu", e)
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Uczeń {name}, średnia wynosi {avg}")
    finally:
        print("Obliczenia zakończone")


# except (ZerodivisionError, TypeError) as e:

liczby()  # ()
liczby(1, 2)  # (1, 2)
liczby(1, 2, 3)  # (1, 2, 3)
# ()
# Bład division by zero
# Obliczenia zakończone
# (1, 2)
# Średnia wynosi 1.5
# Obliczenia zakończone
# (1, 2, 3)
# Średnia wynosi 2.0
# Obliczenia zakończone
liczby("A", 1, 2)
# Bład unsupported operand type(s) for +=: 'int' and 'str'
# Obliczenia zakończone
# ()
# Dzielenie przez zero lub błąd typu division by zero
# Obliczenia zakończone
liczby("Radek", 4, 5, 5, 6, 5, 4)  # Uczeń Radek, średnia wynosi 4.833333333333333
