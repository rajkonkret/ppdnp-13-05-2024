tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst2 = tekst.upper()  # WITAJ ŚWIECIE
print(tekst2)  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie

tekst3 = tekst.lower()
print(tekst3)  # witaj świecie
print(tekst)  # Witaj świecie

print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst)  # Witaj świecie

tekst4 = "Witaj dobry świecie"
print(tekst4.replace("dobry ", ""))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1
# Witaj świecie
# 0123456789
# start 0, stop 4
# Wita 0123 - z prawej strony zbiór otwarty
print(tekst.count("i", 5, 9))  # " świ" indeksy - 5678, 1
print(tekst.count("j", 0, 4))  # 0
print(tekst)  # Witaj świecie
print(tekst[3])  # "a"

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'  b - zapis bajtowy
# liczba w kodzie szesnastkowym \xc5
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b Dodatkowe zdanie"
# f - f-string - tekst sformatowany
# w {} wpisujemy zawartość zmiennej
print(tekst_format)
# "	  Mam na imię Radek
#  i lubię Pythona Dodatkowe zdanie"
# \ - znak ucieczki - znak po tym znaku jest znakiem sterującym
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - oczekuje stringa
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy
Tekst dodatkowy""")
# "Tekst
#     wielolinijkowy
# Tekst dodatkowy"
