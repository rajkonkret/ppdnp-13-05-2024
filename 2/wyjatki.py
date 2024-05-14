# wyjątki - rzucanie, obsługa
# powinniśmy przechwycić i własciwie obsłużyc

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\projekty\ppdnp-13-05-2024\2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print(5 / "00")
    # print("A" + 9)
    # print(int("A"))
    wynik = 5 / 1
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # łapie pozostałe błędy
    print("Błąd", e)
else:  # wykona się tylko, gdy nie ma błędu
    print("Wynik:", wynik)  # Wynik: 5.0
finally:  # wykona się zawsze
    print("Skońćzyłem działanie")

print("Program nadal działa")
# try - except [else - finally]
