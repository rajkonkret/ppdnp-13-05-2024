import sys  # import - dołączanie biblioteki

# sys - biblioteka systemowa

print()  # wypisz/wydrukuj
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
# ctrl - d - powiela linijki
print('Nazywam się Radek')
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\projekty\ppdnp-13-05-2024\pierwszy.py", line 10
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
# ctrl / - komentarz zaznaczonego bloku
# type() - wypisanie typu
print(type("Nazywam się Radek"))  # <class 'str'> typ tekstowy
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'> typ liczbowe, liczby całkowite
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
print(39 + 39)  # standardowe dodawanie 78
print("39" + "39")  # 3939 - konkatenacja - łączenie tekstów
# silne typowanie - sam typów nie zamienia
print(int("39") + 39)  # int() - rzutowanie na liczbę int 78
print(str(39) + "39")  # str() - rzutownaie na tekst str 3939
print("8" + "8" + "8" + "8" + "8")  # 88888
print(8 + 8 + 8 + 8 + 8)  # 40

print(5 * "4")  # 44444

# zmienna - pudełko na dane (koszyczek, worek)
# zmienna moe przechowywac jedną wartośc na raz
# w Pythonie w kązdej chwili moożemy w zmiennej umieścić daną dowolnego typu
# snake_case
# nazwa powinna sugerowac co przechowuje zmienna

name = "Radek"
print(type(name))  # <class 'str'>
print(name)  # wypisanie zawartości zmiennej -> Radek

name = 56
print(name)  # 56
print(type(name))  # <class 'int'>

name: str = 90  # tylko opis, podpowiedź, hint
print(name)  # 90
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))
# dodana wartośc do brancha fix-teskst
